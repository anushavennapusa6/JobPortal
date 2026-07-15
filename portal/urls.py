from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('apply/<int:job_id>/', views.apply, name='apply'),
    path('my-applications/', views.my_applications, name='my_applications'),

    path('delete-application/<int:id>/', views.delete_application, name='delete_application'),
    path('profile/', views.profile, name='profile'),
    path('change-password/', views.change_password, name='change_password'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]