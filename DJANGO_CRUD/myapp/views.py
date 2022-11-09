from django.shortcuts import render,redirect
from .forms import employeeform
from .models import employee

def home(request):
    obj=employee.objects.all()
    return render(request,'home.html',{'data':obj})

def create(request):
    if request.method=='POST':
        form=employeeform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('read')
        return redirect('create')
    else:
        form=employeeform()
    return render(request,'create.html',{'form':form})



def update(request,id):
    obj=employee.objects.get(id=id)
    if request.method=='POST':
        form=employeeform(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            return redirect('read')
        return redirect('create')
    else:
        form=employeeform()
    return render(request,'update.html',{'form':form})
        

def delete(request,id):
    obj=employee.objects.get(id=id)
    if request.method=='POST':
        obj.delete()
        return redirect('read')
    return render(request,'delete.html')
