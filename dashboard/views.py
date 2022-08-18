from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView


# Create your views here.
def index(request):
    # if request.method == 'PSOT':
    #     print ('hello')
    # return HttpResponse("Hello Home")
    return render(request, "home/index.html")

def profile(request):
    # if request.method == 'PSOT':
    #     print ('hello')
    # return HttpResponse("Hello Home")
    return render(request, "home/profile.html")
