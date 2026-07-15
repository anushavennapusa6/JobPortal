from django.shortcuts import render, redirect
from django.contrib import messages
from .models import JobSeeker, Job, Application
# Create your views here.
def home(request):
   if 'username' not in request.session:
        return redirect('login')

   search = request.GET.get('search')
   print(search)
   
   if search:
    jobs = Job.objects.filter(title__icontains=search)
    print(jobs)
   else:
    jobs = Job.objects.all()

   context = {
    'username': request.session['username'],
    'jobs': jobs
   }
   return render(request, 'home.html', context)
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
          request.session['username'] = user.username
          return redirect('home')
        else:
          messages.error(request, "Invalid Username or Password")
    return render(request, 'login.html')
def logout(request):
   request.session.flush()
   return redirect('login')

def apply(request, job_id):

    job = Job.objects.get(id=job_id)

    if request.method == "POST":

        fullname = request.POST['fullname']
        email = request.POST['email']
        phone = request.POST['phone']
        resume = request.FILES['resume']

        Application.objects.create(
            fullname=fullname,
            email=email,
            phone=phone,
            resume=resume,
            job=job
        )

        messages.success(request, "Application Submitted Successfully!")

        return redirect('home')

    return render(request, 'apply.html', {'job': job})

def delete_application(request, id):
  application = Application.objects.get(id=id)
  application.delete()
  messages.success(request, "Application Deleted Successfully!")
  return redirect('my_applications')
def profile(request):
    if 'username' not in request.session:
        return redirect('login')

    user = JobSeeker.objects.get(username=request.session['username'])

    if request.method == "POST":
        print("Profile Update Clicked")
        print(request.POST)

        user.fullname = request.POST.get('fullname')
        user.email = request.POST.get('email')
        user.save()

        print(user.fullname)
        print(user.email)

        messages.success(request, "Profile Updated Successfully!")
        return redirect('profile')

    return render(request, 'profile.html', {'user': user})
def my_applications(request):
  
  if 'username' not in request.session:
    return redirect('login')
  
  applications = Application.objects.all()
  
  context = {
    'applications': applications
  }
  
  return render(request, 'my_applications.html', context)

def change_password(request):
  if 'username' not in request.session:
    return redirect('login')

  user = JobSeeker.objects.get(username=request.session['username'])

  if request.method == "POST":
    old_password = request.POST['old_password']
    new_password = request.POST['new_password']
    confirm_password = request.POST['confirm_password']
    
    if user.password != old_password:
      messages.error(request, "Old Password is incorrect")
    elif new_password != confirm_password:
      messages.error(request, "New Passwords do not match")
    else:
      user.password = new_password
      user.save()
      messages.success(request, "Password Changed Successfully!")
      return redirect('profile')
  return render(request, 'change_password.html') 

def about(request):
  return render(request, 'about.html')


def contact(request):
  return render(request, 'contact.html')