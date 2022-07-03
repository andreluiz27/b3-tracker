from django.shortcuts import render

from django.http import HttpResponse
from celery import shared_task
from b3_tracker.celery import app


@shared_task()
def print_hello_world():
    print("aaaaaaaaaaaaaaaaaaaa")
    return "AAAAAAAAAAAAAAAAAAAAAA"


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
