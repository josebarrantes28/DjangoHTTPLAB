from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):

    html = (
        "<html><body><h1>Error</h1></body></html>"
    )
    return HttpResponse(html, charset="utf-8")