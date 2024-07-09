from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required(login_url='login')
def chatbot(request):
    return render(request,'chatbot.html')

@login_required(login_url='login')
def FindJobPage(request):
    return render(request, 'findjob.html')