from click import password_option
from django.shortcuts import redirect, render
from django.contrib import admin
from .models import Profile
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    context = 'index'
    return render(request,'myApp/index.html',context={'page':context})


def user_register(request):
    context = 'register'

    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        conform_password = request.POST.get('conform_password')
        
        
        user = User.objects.create(
        username=username,
        email=email
        )
        if password==conform_password:
            user.set_password(password)
    
        user.save()

        return redirect('/myApp/user_register')

    return render(request, 'myApp/register.html',context={'page':context})


def user_login(request):
    return render(request, 'myApp/basic.html')

def user_profile(request):
    context = "profile"
    profile_data = Profile.objects.all()
    print(profile_data)
    print(type(profile_data))
    return render(request,"myApp/profile.html",context={'profile':profile_data})