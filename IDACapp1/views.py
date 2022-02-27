from django.shortcuts import render,HttpResponse

# Create your views here.
def index (request):
    return render(request,'index1.html')
    #return HttpResponse("This is index page")
def explore (request):
    return render(request,'Explore.html')
def about (request):
    return render(request,'about.html')
def contact (request):
    return render(request,'Contact.html')
def signin (request):
    return render(request,'signin.html')
def login (request):
    return render(request,'login.html')