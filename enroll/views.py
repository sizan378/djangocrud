from django.shortcuts import render, HttpResponseRedirect
from .models import User
from .forms import studentforms
from django.contrib import messages

def add_show(request):
    student = User.objects.all()
    if request.method == 'POST':
        fm = studentforms(request.POST)
        if fm.is_valid():
            name = fm.cleaned_data['name']
            email = fm.cleaned_data['email']
            password = fm.cleaned_data['password']
            reg = User(name=name,email=email,password=password)
            reg.save()
            messages.add_message(request,messages.SUCCESS, 'Your list add successfully')
            fm = studentforms()
    else:
        fm = studentforms()

    return render(request,'enroll/addshow.html', {'form':fm, 'student':student})

def update_data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        fm = studentforms(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = User.objects.get(pk=id)
        fm = studentforms(instance=pi)
        # return HttpResponseRedirect('/')
    return render(request, 'enroll/update.html', {'forms':fm})

def delete_data(request,id):
    if request.method == 'POST':
        data = User.objects.get(pk=id)
        data.delete()
        return HttpResponseRedirect('/')