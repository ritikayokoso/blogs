from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required

# Create your views here.
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
           auth.login(request, user)
           return redirect("/")
        else:
            messages.info(request, "invalid credentials")
            return redirect('register')
    else:
        return render(request, 'login.html')
def register(request):
    if request.method == 'POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        password=request.POST['password']
        passconf=request.POST['confirmpassword']
        if password==passconf:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return render(request, 'signup.html') 
            user = User.objects.create_user(username=username, password=password, first_name=first_name, last_name=last_name)
            user.save()
            print(user)
        return render(request, 'login.html') 
    else:

     return render(request, 'signup.html') 
     
@login_required
def home(request):
    return render(request, "index.html")