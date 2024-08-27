from django.contrib.auth.decorators import login_required
from django.shortcuts import render
import requests

@login_required(login_url='login')
def aboutus(request):
    return render(request,'chatbot.html')

@login_required(login_url='login')
def FindJobPage(request):
    return render(request, 'findjob.html')