from django.template import loader

from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from tracker_app.serializers import StockTrackerSeralizer
from tracker_app.tasks import create_periodic_task
from tracker_app.models import StockDomain
from django.shortcuts import redirect
from django_celery_beat.models import PeriodicTask


def index(request):
    template = loader.get_template("tracker_app/index.html")
    return HttpResponse(template.render())


def stocks_page(request):
    template = loader.get_template("tracker_app/stocks.html")
    all_tracking_task = PeriodicTask.objects.all()
    tracking_task_list = []
    for task in all_tracking_task:

        # let's not list any celery related task
        # TODO should be refactored after
        if "celery" not in task.name:
            tracking_task_list.append(task.name)
        else:
            continue

    context = {"symbols": tracking_task_list}
    return HttpResponse(template.render(context, request))


def tracking_forms_page(request):
    template = loader.get_template("tracker_app/tracking_forms.html")
    stocks_domain = StockDomain.objects.all()
    symbols_list = [stock.symbol for stock in stocks_domain]
    context = {"symbols": symbols_list}
    template = loader.get_template("tracker_app/stocks.html")
    return HttpResponse(template.render(context, request))


def tracked_stock_detail(request, stock_symbol):
    template = loader.get_template("tracker_app/stocks.html")
    print(stock_symbol)
    return HttpResponse(template.render())


class StartTrackingView(APIView):
    def post(self, request):
        data = {"symbol": request.data.get("stock"), "interval": "test"}

        stock_tracker_serializer = StockTrackerSeralizer(data=data)
        if stock_tracker_serializer.is_valid():
            create_periodic_task(stock_tracker_serializer.data.get("symbol"))
            # TODO write a user return in case already has

            return redirect("/tracker_app/tracking-forms")
        else:
            return Response({"message": "Not valid data"})
