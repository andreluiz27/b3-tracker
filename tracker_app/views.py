from requests import request
from rest_framework.response import Response
from django_celery_beat.models import PeriodicTask, IntervalSchedule
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from tracker_app.serializers import StockTrackerSeralizer
from rest_framework import generics



def create_periodic_task():
   # interval = IntervalSchedule.objects.
    PeriodicTask.objects.create(interval=IntervalSchedule.objects.all().first(),
                                name="Testing",
                                task='stock_tracker'
                                
                                  )
@api_view(['GET'])
def index(request):
    # api.stock_tracker()
  #  create_periodic_task()
    return Response({"message": "Backend is running"})

@api_view(['POST'])
def start_tracking(request):
    # api.stock_tracker()
   # create_periodic_task()
    return Response({"message": "Tracker has just started"})

class StartTrackingView(generics.CreateAPIView):

    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAdminUser]
    serializer_class = StockTrackerSeralizer
    def post(self, request) :
        return Response({"message": "Tracker has just started"})
