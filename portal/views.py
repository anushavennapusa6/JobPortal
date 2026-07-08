from django.shortcuts import render, redirect
from django.contrib import messages
from .models import JobSeeker
# Create your views here.
def home(request):
    return render(request, 'home.html')
def register(request):
  if request.method == "POST":
    print("Form Submitted")
    fullname = request.POST['fullname']
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    confirm_password = request.POST['confirm_password']
    print(fullname)
    print(username)
    print(email)
    print(password)
    print(confirm_password)
    if password != confirm_password:
      messages.error(request, "Passwords do not match")
      return render(request, 'register.html')
    if JobSeeker.objects.filter(username=username).exists():
      messages.error(request, "Username already exists")
      return render(request, 'register.html')
    JobSeeker.objects.create(
      fullname=fullname,
      username=username,
      email=email,
      password=password
)
  return render(request, 'register.html')
def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        print(username)
        print(password)
        user = JobSeeker.objects.filter(
          username=username,
          password=password
        ).first()
        if user:
          return redirect('home')
        else:
          messages.error(request, "Invalid Username or Password")
    return render(request, 'login.html')