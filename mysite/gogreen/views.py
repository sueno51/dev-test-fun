from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("Welcome!! You are at test site.")

def locationdetail(request,question_id):
    return HttpResponse("You're looking at location %s." % question_id)

def locationinfo(request,question_id):
    response = "You're looking at information about location %s."
    return HttpResponse(response % question_id)

def vote(request,question_id):
    return HttpResponse("You're voting on question %s." % question_id)


