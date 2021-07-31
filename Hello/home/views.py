from django.shortcuts import render , HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("this is Homepage")

    
def about(request):
    return HttpResponse("this is About Page")

