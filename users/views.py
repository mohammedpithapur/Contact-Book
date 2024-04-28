from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
def login_user(request):
    if request.method =="POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('list')
        else:
            messages.success(request, ('There was an error logging in ,Try again'))
            return redirect('login')
    else:
        return render(request, 'registration/login.html', {})
def logout_user(request):
    logout(request)
    messages.success(request,('Successfully logged out'))
    return redirect('login')
def registr_user(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            user=authenticate(username=username,password=password)
            return redirect('login')
    else:
        form=UserCreationForm()
    return render(request, 'registration/register.html',{'form':form})