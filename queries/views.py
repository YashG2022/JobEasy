from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import UserQuery
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.
# views.py
@login_required
def contactus(request):
    if request.method == 'POST':
        query_text = request.POST.get('query')  # Get the query from the form
        if query_text:
            user_query =UserQuery.objects.create(user=request.user, query=query_text)
            send_mail(
                subject='New Query Submitted',
                message=f'User {request.user} has submitted a new query:\n\n{query_text}',
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=['yashgautam2003@gmail.com','21ucs165@lnmiit.ac.in'],  # Replace with your admin email
            )
            return render(request, 'contact_us.html') # Redirect to a success page after submission
    return render(request, 'contact_us.html')
