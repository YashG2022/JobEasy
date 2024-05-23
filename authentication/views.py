#Create your views here.
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='login')
def HomePage(request):
    return render(request, 'home.html')

@login_required(login_url='login')
def chatbot(request):
    return render(request,'chatbot.html')
def SignupPage(request):
    if request.method == 'POST':
        fname=request.POST.get('firstname')
        lname=request.POST.get('lastname')
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        if pass1 != pass2:
            return HttpResponse("Your password and conform password are not Same!!")
        else:
            my_user = User.objects.create_user(uname, email, pass1)
            print(fname)
            print(lname)
            my_user.first_name=fname
            my_user.last_name=lname
            print(fname)
            print(lname)
            my_user.save()
            return redirect('login')

    return render(request, 'signup.html')


def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')
        user = authenticate(request, username=username, password=pass1)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse("Username or Password is incorrect!!!")
        
    return render(request, 'login.html')


def LogoutPage(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def FindJobPage(request):
    return render(request, 'findjob.html')