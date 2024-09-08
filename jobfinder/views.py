from .data_getter import jobs
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseForbidden
from jobfinder.models import JobListing


# def admin_required(view_func):
#     decorated_view_func = user_passes_test(
#         lambda user: user.is_superuser,
#         login_url='/admin/login/'
#     )(view_func)
#     return decorated_view_func

# @admin_required
# def jobloader(request):
#     # Your logic here
#     return render(request, 'loader.html')


# @admin_required
# def softdevloader(request):
#     jobs("Software Developer")
#     # return render(request, 'softdev.html', {'jobs': job_listings})
#     return render(request, 'loader.html')


# @admin_required
# def uiuxloader(request):
#     jobs("UI UX")
#     return render(request, 'loader.html')

# @admin_required
# def gdloader(request):
#     jobs("Graphic Designer")
#     return render(request, 'loader.html')

# @admin_required
# def appdevloader(request):
#     jobs("App Developer")
#     return render(request, 'loader.html')

# @admin_required
# def aimlloader(request):
#     jobs("AI ML")
#     return render(request, 'loader.html')

@login_required(login_url='login')
def softdev(request):
    jobs = JobListing.objects.filter(job_type="Software Developer")
    # Render the jobs to the template
    return render(request, 'jobpage.html', {'jobs': jobs})


@login_required(login_url='login')
def uiux(request):
    jobs = JobListing.objects.filter(job_type="UI UX")
    # Render the jobs to the template
    return render(request, 'jobpage.html', {'jobs': jobs})

@login_required(login_url='login')
def gd(request):
    jobs = JobListing.objects.filter(job_type="Graphic Designer")
    # Render the jobs to the template
    return render(request, 'jobpage.html', {'jobs': jobs})

@login_required(login_url='login')
def appdev(request):
    jobs = JobListing.objects.filter(job_type="App Developer")
    # Render the jobs to the template
    return render(request, 'jobpage.html', {'jobs': jobs})

@login_required(login_url='login')
def aiml(request):
    jobs = JobListing.objects.filter(job_type="AI ML")
    # Render the jobs to the template
    return render(request, 'jobpage.html', {'jobs': jobs})