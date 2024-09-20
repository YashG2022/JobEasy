from django.contrib import admin
from django.urls import path
from authentication import views as authviews
from jobfinder import views as finderviews
from . import views as JobEasy
from chatbot import views as chatbotviews
from queries import views as queriesviews
from jobfinder.tasks import start_background_job_loader

start_background_job_loader()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',authviews.SignupPage,name='signup'),
    # path('jobloader/',finderviews.jobloader,name='jobloader'),
    path('findjob/',JobEasy.FindJobPage,name='findjob'),
    path('softdev/',finderviews.softdev,name='softdev'),
    path('uiux/',finderviews.uiux,name='uiux'),
    path('gd/',finderviews.gd,name='gd'),
    path('appdev/',finderviews.appdev,name='appdev'),
    path('aiml/',finderviews.aiml,name='aiml'),
    # path('softdevloader/',finderviews.softdevloader,name='softdevloader'),
    # path('uiuxloader/',finderviews.uiuxloader,name='uiuxloader'),
    # path('gdloader/',finderviews.gdloader,name='gdloader'),
    # path('appdevloader/',finderviews.appdevloader,name='appdevloader'),
    # path('aimlloader/',finderviews.aimlloader,name='aimlloader'),
    path('chatbot',chatbotviews.chatbot,name='chatbot'),
    path('login/',authviews.LoginPage,name='login'),
    path('home/',authviews.HomePage,name='home'),
    path('logout/',authviews.LogoutPage,name='logout'),
    path('aboutus/',JobEasy.aboutus,name='aboutus'),
    path('contactus/',queriesviews.contactus,name='contactus'),
]