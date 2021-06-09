from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

def index_view(request):
    return HttpResponse('<h1>Home Page</h1>')


def about_view(request):
    return HttpResponse('<h1>About Page</h1>')


def contact_view(request):
    return HttpResponse('<h1>Contact Page</h1>')