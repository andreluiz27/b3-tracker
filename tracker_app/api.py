"""
Handles external api connection to fetch b3 data
"""
from celery import shared_task

from yahooquery import Ticker
from tracker_app import models

@shared_task()
def stock_tracker():

    stock = Ticker("PETR4.SA")

    # df, i.e, a dataframe type
    stock_df_time_serie = stock.history(period="1d", interval="30m")

    # get first row
    stock_df_first_row = stock_df_time_serie.head(1)

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
    stock_tracker_model.save() 


petr = Ticker("PETR4.SA")
a = petr.history(period="1d", interval="30m")

print(a)
