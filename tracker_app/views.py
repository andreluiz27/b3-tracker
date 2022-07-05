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


def index(request):
  template = loader.get_template('tracker_app/index.html')

  return HttpResponse(template.render())

def stocks_page(request):
  template = loader.get_template('tracker_app/stocks.html')
  return HttpResponse(template.render())
  
def tracking_forms_page(request):
  template = loader.get_template('tracker_app/tracking_forms.html')
  return HttpResponse(template.render())


class StartTrackingView(APIView):

    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAdminUser]

    def post(self, request):
        stock_tracker_serializer = StockTrackerSeralizer(data=request.data)
        if stock_tracker_serializer.is_valid():
            create_periodic_task(stock_tracker_serializer.data.get('symbol'))
            return Response({"message": "Tracker has just started"})
        else:
             return Response({"message": "Not valid data"})
            