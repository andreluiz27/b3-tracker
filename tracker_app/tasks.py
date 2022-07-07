"""
Handles external api connection to fetch b3 data
"""
from celery import shared_task
from django.core.mail import send_mail

from yahooquery import Ticker
import logging
from django_celery_beat.models import PeriodicTask, IntervalSchedule
from tracker_app import models
import json
import pandas as pd
from b3_tracker.settings import EMAIL_SENDER, EMAIL_RECEIVER


def create_periodic_task(stock_name):
    # interval = IntervalSchedule.objects.
    tracking_task, created = PeriodicTask.objects.get_or_create(
        interval=IntervalSchedule.objects.all().first(),
        name=stock_name,
        args=json.dumps(
            [
                stock_name,
            ]
        ),
        task="stock_tracker",
    )

    return created


@shared_task(name="stock_tracker")
def stock_tracker(stock_name):

    stock = Ticker(stock_name)
    logging.info(stock)

    # df, i.e, a dataframe type
    stock_df_time_serie = stock.history(period="1d", interval="1m")
    logging.info(stock_df_time_serie)

    if isinstance(stock_df_time_serie, pd.DataFrame):
        # get first row
        stock_df_first_row = stock_df_time_serie.tail(1)

        # It's a multi index situation
        symbol = stock_df_first_row.index[0][0]  # symbol it's a index
        dt_time = stock_df_first_row.index[0][1]  # date it's a index

        open_value = float(stock_df_first_row.open.values)
        low_value = float(stock_df_first_row.low.values)
        high_value = float(stock_df_first_row.high.values)
        close_value = float(stock_df_first_row.close.values)
        volume = int(stock_df_first_row.volume.values)
        interval = "30m"

        # saving in database
        stock_tracker_model = models.StockTracker(
            symbol=symbol,
            dt_time=dt_time,
            open_value=open_value,
            low_value=low_value,
            high_value=high_value,
            close_value=close_value,
            volume=volume,
            interval=interval,
        )
        stock_trigger_model = models.StockTrigger.objects.filter(
            stock__symbol=stock_name
        ).first()

        # Bad if logic, should be refactored!!!!
        if stock_trigger_model and close_value > stock_trigger_model.upper_close_limit:
            logging.info("Stock reached upper limit")

            stock_trigger_model.was_triggered = True
            stock_trigger_model.save()

            send_mail(
                "Subject here",
                f"{stock_name} reached close value upper limit of {close_value}",
                EMAIL_SENDER,
                [EMAIL_RECEIVER],
                fail_silently=False,
            )

        if stock_trigger_model and close_value < stock_trigger_model.lower_close_limit:
            logging.info("Stock reached lower limit")

            stock_trigger_model.was_triggered = True
            stock_trigger_model.save()

            send_mail(
                "Subject here",
                f"{stock_name} reached close value lower limit of {close_value}",
                EMAIL_SENDER,
                [EMAIL_RECEIVER],
                fail_silently=False,
            )

        stock_tracker_model.save()

    else:
        logging.info(
            f"Not a data frame, what we have is type {type(stock_df_time_serie)} and his content {stock_df_time_serie} "
        )
