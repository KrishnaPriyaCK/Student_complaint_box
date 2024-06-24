from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.hashers import check_password
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from .models import *

def index(request):
    return render(request, 'index.html')

def studentreg(request):
    if request.method == 'POST':
        userphoto = request.FILES['userphoto']
        up = FileSystemStorage()
        img = up.save(userphoto.name, userphoto)
        useremail = request.POST.get('useremail')
        username = request.POST.get('username')
        userphone = request.POST.get('userphone')
        password = request.POST.get('password')
        log = register(useremail=useremail, username=username, userphone=userphone, password=password, userphoto=userphoto)
        log.save()
        return redirect(index)
    return render(request, 'register.html')

def studentlog(request):
    if request.method == 'POST':
        useremail = request.POST.get('useremail')
        password = request.POST.get('password')

        if useremail == 'admin@gmail.com' and password == 'admin':
            request.session['adminemail'] = useremail
            request.session['admin'] = 'admin'
            return render(request, 'index.html', {'status': 'Admin login successful'})

        elif register.objects.filter(useremail=useremail, password=password).exists():
            sdet = register.objects.get(useremail=useremail, password=password)
            request.session['student'] = sdet.id
            request.session['username'] = sdet.username
            request.session['useremail'] = sdet.useremail
            request.session['students'] = 'students'
            return render(request, 'index.html')
        

        else:
            return render(request, 'studentlogin.html', {'status': 'Incorrect credentials'})
        
    return render(request, 'studentlogin.html') 

def cmpltform(request):
    if request.method == 'POST':
        f=request.session['student']
        u=complaint.objects.filter(userid=f)
        complaintto = request.POST.get('complaintto')
        date = request.POST.get('date')
        name = request.POST.get('name')
        email = request.POST.get('email')
        complaintmesg = request.POST.get('complaintmesg')
        status = request.POST.get('status')
        log = complaint(userid=f,complaintto=complaintto, date=date, name=name, email=email, complaintmesg=complaintmesg, status=status)
        log.save()

    return render(request, 'complaintform.html')

def logout(request):
    session_keys = list(request.session.keys())
    for key in session_keys:
        del request.session[key]
    return redirect(index)

def facultyreg(request):
    if request.method == 'POST':
        designation = request.POST.get('designation')
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        log = faculty(designation=designation, name=name, email=email, password=password)
        log.save()
        return redirect(index)


    return render(request, 'facultyregister.html')


def facultylog(request):
    if request.method == 'POST':
        designation = request.POST.get('designation')
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            fdet = faculty.objects.get(designation=designation, email=email, password=password)
        except faculty.DoesNotExist:
            return render(request, 'facultylogin.html', {'status': 'Incorrect credentials'})

        request.session['faculty'] = fdet.id
        request.session['name'] = fdet.name
        request.session['email'] = fdet.email
        request.session['fdesig'] = fdet.designation

        request.session['faculties'] = 'faculties'
        return render(request, 'index.html')
        
    else:
        return render(request, 'facultylogin.html', {'status': ''})


def viewcomplaint(request):
    t=request.session['fdesig']
    u=complaint.objects.filter(complaintto=t)
    return render(request,'complaintview.html',{'res':u})

def profilefaculty(request):
    s=request.session['faculty']
    m=faculty.objects.get(id=s)
    return render(request,'facultyprofile.html',{'res':m})


def ackform(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        date = request.POST.get('date')
        email = request.POST.get('email')
        ackmesg = request.POST.get('ackmesg')
        log = acknowledgement(name=name,date=date,email=email,ackmesg=ackmesg)
        log.save()
        return redirect(ackform)
    return render(request, 'acknowledgement.html')
    
def ackview(request):
    m=request.session['useremail']
    n=acknowledgement.objects.filter(email=m)
    return render(request,'acknowledgementview.html',{'res':n})

def viewfaculty(request):
    u=faculty.objects.all()
    return render(request,'facultyview.html',{'res':u})

def viewadmin(request):
    return render(request, 'adminprofile.html')

def viewstudent(request):
    u=register.objects.all()
    return render(request,'studentview.html',{'res':u})

def sdelete(request,id):
    mark=register.objects.get(pk=id)
    mark.delete()
    return redirect(viewstudent)

def cmpltviewadmin(request):
    u=complaint.objects.all()
    return render(request,'complaintviewadmin.html',{'res':u})

def ackfaculty(request):
    if request.method == 'POST':
        date = request.POST.get('date')
        designation=request.POST.get('designation')
        name = request.POST.get('name')
        email = request.POST.get('email')
        ackmesg = request.POST.get('ackmesg')
        log = facack(date=date,designation=designation,name=name,email=email,ackmesg=ackmesg)
        log.save()

    return render(request, 'facultyackadmin.html')

def viewfacultyack(request):
    t=request.session['email']
    u=request.session['fdesig']
    h=facack.objects.filter(email=t,designation=u)
    return render(request,'viewfacultyackadmin.html',{'res':h})

def cupdate(request,id):
    cm=complaint.objects.get(pk=id)
    return render(request,'complaintupdate.html',{'res':cm})

def cmupdate(request, id):
    cm = complaint.objects.get(pk=id)
    
    if request.method == 'POST':
        complaintto = request.POST.get('complaintto')
        date = request.POST.get('date')
        name = request.POST.get('name')
        email = request.POST.get('email')
        complaintmesg = request.POST.get('complaintmesg')
        status = request.POST.get('status')
        userid = cm.userid
        log = complaint(id=id, userid=userid, complaintto=complaintto, date=date, name=name, email=email, complaintmesg=complaintmesg, status=status)
        log.save()
        return redirect(viewcomplaint)
    return render(request, 'complaintform.html', {'res': cm})


def profilestudent(request):
    s=request.session['student']
    m=register.objects.get(id=s)
    return render(request,'profile.html',{'res':m})
def supdate(request):
    s=request.session['student']
    m=register.objects.get(id=s)
    return render(request,'studentupdate.html',{'res':m})

def updatestudent(request,id):
    if request.method == 'POST':
        userphoto = request.FILES['userphoto']
        up = FileSystemStorage()
        img = up.save(userphoto.name, userphoto)
        useremail = request.POST.get('useremail')
        username = request.POST.get('username')
        userphone = request.POST.get('userphone')
        password = request.POST.get('password')
        log = register(useremail=useremail, username=username, userphone=userphone, password=password, userphoto=userphoto,id=id)
        log.save()
        return redirect(profilestudent)
    return render(request, 'register.html')





























