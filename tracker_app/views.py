from django.shortcuts import render

from django.http import HttpResponse
from celery import shared_task
from tracker_app import api


@shared_task()
def print_hello_world():
    print("aaaaaaaaaaaaaaaaaaaa")
    return "AAAAAAAAAAAAAAAAAAAAAA"


def index(request):
    api.stock_tracker()
    return HttpResponse("Hello, world. You're at the polls index.")
