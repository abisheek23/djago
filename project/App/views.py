from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def fun1(request):
    return HttpResponse('django')
def fun2(request):
    return render(request,'demo.html')
def fun3(req):
    return render(req,'home.html')
def fun4(req):
    return render(req,'about.html')
def fun5(req):
    return render(req,'contact.html')