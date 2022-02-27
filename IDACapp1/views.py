from django.shortcuts import render,HttpResponse

# Create your views here.
def index (request):
    return render(request,'index1.html')
    #return HttpResponse("This is index page")
def explore (request):
    return render(request,'Explore.html')