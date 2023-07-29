from click import password_option
from django.shortcuts import redirect, render
from django.contrib import admin
from .models import Profile
from django.contrib.auth.models import User
from . forms import RegistrationForm

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
