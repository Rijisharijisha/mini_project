from django.shortcuts import render
from templeapp.models import temptb
from templeapp.models import festtb
from templeapp.models import vazhitb


# Create your views here.






def addtem(request):
    if request.method=='POST':
        obj=temptb()
        obj.name=request.POST.get('name')
        obj.address=request.POST.get('address')
        obj.time=request.POST.get('time')
        obj.contact=request.POST.get('contact')
        obj.save()
    
    return render(request,'templeadmin/tempadd.html')

def vitem(request):
    obj=temptb.objects.all()
    return render(request,'templeadmin/tempview.html',{'data':obj})

def temupdate(request,pk):
    obj=temptb.objects.get(temp_id=pk)
    if request.method=='POST':
        obj=temptb.objects.get(temp_id=pk)
        obj.name=request.POST.get('name')
        obj.address=request.POST.get('address')
        obj.time=request.POST.get('time')
        obj.contact=request.POST.get('contact')
        obj.save()
    return render(request,'templeadmin/tempupdate.html',{'data':obj})

def temdelete(request,pk):
    obj=temptb.objects.get(temp_id=pk)
    obj.delete()
    return vitem(request)







def addfest(request):
    if request.method=='POST':
        obj=festtb()
        obj.name=request.POST.get('name')
        obj.time=request.POST.get('time')
        obj.description=request.POST.get('description')
        obj.save()

    return render(request,'templeadmin/festadd.html')

def vifest(request):
    obj=festtb.objects.all()
    return render(request,'templeadmin/festview.html',{'data':obj})

def festupdate(request,pk):
    obj=festtb.objects.get(fest_id=pk)
    if request.method=='POST':
        obj=festtb.objects.get(fest_id=pk)
        obj.name=request.POST.get('name')
        obj.time=request.POST.get('time')
        obj.description=request.POST.get('description')
        obj.save()
    return render(request,'templeadmin/festupdate.html',{'data':obj})

def festdelete(request,pk):
    obj=festtb.objects.get(fest_id=pk)
    obj.delete()
    return vifest(request)







def addvazhi(request):
    if request.method=='POST':
        obj=vazhitb()
        obj.name=request.POST.get('name')
        obj.price=request.POST.get('price')
        obj.save()

    return render(request,'templeadmin/vazhiadd.html')

def vivazhi(request):
    obj=vazhitb.objects.all()
    return render(request,'templeadmin/vazhiview.html',{'data':obj})

def vazhiupdate(request,pk):
    obj=vazhitb.objects.get(vazhi_id=pk)
    if request.method=='POST':
        obj=vazhitb.objects.get(vazhi_id=pk)
        obj.name=request.POST.get('name')
        obj.price=request.POST.get('price')
        obj.save()
    return render(request,'templeadmin/vazhiupdate.html',{'data':obj})

def vazhidelete(request,pk):
    obj=vazhitb.objects.get(vazhi_id=pk)
    obj.delete()
    return vivazhi(request)


