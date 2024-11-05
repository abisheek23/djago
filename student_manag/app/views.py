from django.shortcuts import render ,redirect

# Create your views here.
std=[{'roll_no':'1','name':'asd','age':'20'},{'roll_no':'2','name':'aws','age':'22'},{'roll_no':'3','name':'sws','age':'23'}]
def home(req):
    if req.method=='POST':
        roll=req.POST['roll_no']
        name=req.POST['name']
        age=req.POST['age']
        std.append({'roll_no':roll,'name':name,'age':age})
        return redirect(home)
    else:
        return render(req,'home.html',{'student':std})
    
def edit_std(req,a):
    data=''
    for i in std:
        if i['roll_no']==a:
            data=i
    if req.method=='POST':
        roll=req.POST['roll_no']
        name=req.POST['name']
        age=req.POST['age']
        data['roll_no']=roll
        data['name']=name
        data['age']=age
        return redirect(home)
    else: 
        return render(req,'edit.html',{'data':data})
 
 
def delete(req,a):
    for i in std:
        if i['roll_no']==a:
            std.remove(i)
        return redirect(home)



        
