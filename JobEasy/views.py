from django.contrib.auth.decorators import login_required
from django.shortcuts import render
import requests


def success_page(request):
    return render(request, 'success_page.html')

@login_required(login_url='login')
def aboutus(request):
    return render(request,'about_us.html')

@login_required(login_url='login')
def FindJobPage(request):
    return render(request, 'findjob.html')

@login_required(login_url='login')
def contactus(request):
    return render(request,'contact_us.html')