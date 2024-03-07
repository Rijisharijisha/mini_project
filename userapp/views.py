from django.shortcuts import render,redirect
from templeapp.models import temptb
from templeapp.models import festtb
from templeapp.models import vazhitb
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required 
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Create your views here.

@login_required
def home(request):
	return render(request,'useradmin/layout/index.html')

def loginview(request):
    uname = request.POST.get('username')
    pwd = request.POST.get('password')
    user = authenticate(request, username=uname, password=pwd)
    if user is not None:
        login(request, user)
        return redirect('home')
    else:
        return render(request,"register/login.html")
        
def logout_view(request):
    logout(request)
    return redirect('login')

def sign_up(request):
        uform = UserCreationForm(request.POST)
        if request.method == "POST":
            if uform.is_valid():
                uname = uform.cleaned_data.get('username')
                pwd = uform.cleaned_data.get('password1')
                email=uform.cleaned_data.get('email')
                user1=User.objects.create_user(username=uname,password=pwd,email=email)
                user1.save()
                user = authenticate(request, username=uname, password=pwd)
                login(request,user)
                return redirect('home')
        else:
            uform = UserCreationForm()
        return render(request, 'register/sign_up.html', {'form': uform})



def vtem(request):
    obj=temptb.objects.all()
    return render(request,'useradmin/tview.html',{'data':obj})


def vfest(request):
    obj=festtb.objects.all()
    return render(request,'useradmin/fview.html',{'data':obj})

def vvazhi(request):
    obj=vazhitb.objects.all()
    return render(request,'useradmin/vview.html',{'data':obj})

def index(request):
    return render(request,'useradmin/layout/index.html')