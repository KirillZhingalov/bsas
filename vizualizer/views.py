from django.shortcuts import render
from django.http import HttpResponse


def index(res):
    return HttpResponse("index page.")
