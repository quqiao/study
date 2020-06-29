from rest_framework import serializers
from rest_framework import viewsets
from django.http import HttpResponse, JsonResponse
from django.http import QueryDict
from rest_framework.request import Request
from hello.models import *

def index(request):
    return HttpResponse("Hello world !  django ~~")
def test(request):
    return HttpResponse("test_page! django")

