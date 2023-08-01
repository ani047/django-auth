from click import password_option
from django.shortcuts import redirect, render
from django.contrib import admin
from .models import Profile
from django.contrib.auth.models import User
from . forms import RegistrationForm

# Create your views here.
def index(request):
    context = 'index'
    users = Profile.objects.all()
    list = []
    for i in users:
        list.append(i.id)
        list.append(i.first_name)
        list.append(i.last_name)
        list.append(i.country)

    return render(request,'myApp/index.html',context={'page':context,'user':list})


def user_register(request):
    context = 'register'

    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        
        user = User.objects.create(
        username=username,
        email=email
        )
        user.set_password(password)
        user.save()
        return redirect('/myApp/user_register')

    return render(request, 'myApp/register.html',context={'page':context})


def user_login(request):
    return render(request, 'myApp/login.html')

def user_profile(request):
    context = "profile"
    profile_data = Profile.objects.all()
    return render(request,"myApp/profile.html",context={'profile':profile_data})

def registeration(request):
    if request.method =='POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.changed_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            conform_password = form.cleaned_data['conform_password']

            if password == conform_password:
                pass
                #user = User.objects.create_user(username = username,email=email,password=password,conform_password = conform_password)                 
                #user.save()
                #return redirect('/myApp/index')
            else:
                form.add_error('conform_password','passwords do dont match')
        else:
            form = RegistrationForm()
        return render(request, 'myApp/registration.html',{'form':form})
