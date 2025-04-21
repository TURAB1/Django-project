from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Asia tour agency!")

def render_template(request):
    return render(request, 'tours/index.html')
