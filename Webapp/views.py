from django.shortcuts import render
from django.shortcuts import render,redirect
from django.contrib import messages
from Webapp.models import Student_Data
from django.http import HttpResponseRedirect
from django.contrib.sessions.models import Session

def Student(request):
    return render(request,'MyApp/Student.html')

def Stud_Save(request):
    sid = request.POST.get("sid")
    name = request.POST.get("name")
    semester = request.POST.get("semester")
    branch = request.POST.get("branch")
    shown = Student_Data.objects.filter(sid=sid)
    if shown.count()>0:
        return render(request, "MyApp/Student.html", {'message':'Student Already Exist' })
    else:
        Student_Data(sid=sid, name=name, semester=semester, branch=branch).save()
        return render(request,'MyApp/Student.html',{'message':'Student Detail Added Succesfully' })


def Stud_Show(request):
   show = Student_Data.objects.all()
   context = {'show':show}
   return render(request, 'MyApp/Showlist.html', context)

#
def Stud_Edit(request):
    id = request.POST.get('sid')
    edit = Student_Data.objects.filter(sid=id)
    return render(request,"MyApp/StudUpdate.html", {'edit':edit})

def Stud_Update(request):
    id = request.POST.get("id")
    sid = request.POST.get("sid")
    name = request.POST.get("name")
    semester = request.POST.get("semester")
    branch = request.POST.get("branch")
    update = Student_Data.objects.filter(sid=sid).update(sid=sid, name=name, semester=semester, branch=branch)
    if update:
        return redirect('show')
    else:
        edit = Student_Data.objects.filter(id=id)
        return render(request, "MyApp/StudUpdate.html", {'edit': edit,'message':'Student with the entered sid doent exist'})


def Delete_Stud(request):
    sid=request.POST.get('sid')
    delete=Student_Data.objects.filter(sid=sid).delete()
    if delete:
        return redirect('show')
    else:
        return render(request,'MyApp/StudUpdate.html',{'message':'Not Deleted'})