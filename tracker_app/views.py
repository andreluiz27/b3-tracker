from requests import request
from django.template import loader

from django.http import HttpResponse
from rest_framework.response import Response
from django_celery_beat.models import PeriodicTask, IntervalSchedule
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from tracker_app.serializers import StockTrackerSeralizer
from rest_framework import generics
from tracker_app.tasks import create_periodic_task
from tracker_app.models import StockDomain
from django.shortcuts import redirect



def index(request):
    template = loader.get_template("tracker_app/index.html")

    return HttpResponse(template.render())


def stocks_page(request):
    template = loader.get_template("tracker_app/stocks.html")

    return HttpResponse(template.render())


def tracking_forms_page(request):
    template = loader.get_template("tracker_app/tracking_forms.html")
    stocks_domain = StockDomain.objects.all()
    symbols_list = [stock.symbol for stock in stocks_domain]
    context = {"symbols": symbols_list}
    return HttpResponse(template.render(context, request))


class StartTrackingView(APIView):
    def post(self, request):
        data = {"symbol": request.data.get("stock"), "interval": "test"}

        stock_tracker_serializer = StockTrackerSeralizer(data=data)
        if stock_tracker_serializer.is_valid():
            create_periodic_task(stock_tracker_serializer.data.get("symbol"))
            return redirect('/tracker_app/tracking-forms')
        else:
            print(stock_tracker_serializer.errors)
            return Response({"message": "Not valid data"})
