from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

def index(request):
    return HttpResponseRedirect(reverse('JandB:home'))

# Create your views here.
def home(request):
    return  render(request, "index.html")

def knowledge(request):
    return  render(request, "knowledge.html")

def mywork(request):
    return  render(request, "mywork.html")
