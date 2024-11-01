from django.shortcuts import render , redirect
from django.http import HttpResponse

# Create your views here.
def fun1(request):
    return HttpResponse('django')

def fun3(req1):
    return render(req1,'home.html')

l=[]
def fun4(req):
    if req.method=='POST':
        name=req.POST['name']
        age=req.POST['age']
        print(name,age)
        l.append({'name':name,'age':age})
        print(l)
        return redirect(fun4)
    else :
        return render(req,'demo.html')
    

l=[{'name': 'sz', 'age': '21'},{'name': 'ab', 'age': '25'}]
def display(req):
    a='welcom'
    return render(req,'display.html',{'data':l,'data1':a})

def add(req):
    if req.method=='POST':
        name=req.POST['name']
        age=req.POST['age']
        print(name,age)
        l.append({'name':name,'age':age})
        print(l)
        return redirect(display)
    else :
        return render(req,'add.html')