from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    # if request.method == 'PSOT':
    #     print ('hello')
    # return HttpResponse("Hello Home")
    return render(request, "home/index.html")