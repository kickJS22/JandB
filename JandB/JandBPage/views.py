from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return  render(request, "index/home/index.html")

def knowledge(request):
    return  render(request, "index/knowledge/knowledge.html")

def mywork(request):
    return  render(request, "index/mywork/mywork.html")
