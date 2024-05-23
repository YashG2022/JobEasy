from django.contrib import admin
from django.urls import path
from authentication import views as authviews
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',authviews.SignupPage,name='signup'),
    path('findjob/',authviews.FindJobPage,name='findjob'),
    path('chatbot',authviews.chatbot,name='chatbot'),
    path('login/',authviews.LoginPage,name='login'),
    path('home/',authviews.HomePage,name='home'),
    path('logout/',authviews.LogoutPage,name='logout'),
]