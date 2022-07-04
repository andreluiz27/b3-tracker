from requests import request
from rest_framework.response import Response
from django_celery_beat.models import PeriodicTask, IntervalSchedule
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from tracker_app.serializers import StockTrackerSeralizer
from rest_framework import generics
from tracker_app.tasks import create_periodic_task


@api_view(["GET"])
def index(request):
    # api.stock_tracker()
    #  create_periodic_task()
    return Response({"message": "Backend is running"})


@api_view(["POST"])
def start_tracking(request):
    # api.stock_tracker()
    # create_periodic_task()
    return Response({"message": "Tracker has just started"})


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
            