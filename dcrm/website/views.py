from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .form import SignUpForm
# Create your views here.
def home(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        #check is the person is in the database
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,'You have successfully logged in')
            return redirect('home')
        else:
            messages.error(request,'Invalid credentials')
    return render(request,'home.html',{})
# def login_user(request):
#     pass
def logout_user(request):
    logout(request)
    messages.success(request,'You have successfully logged out')
    return redirect('home')
def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username,password=password)
            messages.success(request,'Account was created for '+username)
            login(request,user)
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request,'register.html',{'form':form})
    return render(request,'register.html',{'form':form})
    