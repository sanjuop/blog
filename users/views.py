from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.shortcuts import render, redirect
from users.forms import RegistrationForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'your account has been created! Now you are able to login')
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'users/register.html', {"form":form})


@login_required
def profile(request):
    return render(request, 'users/profile.html')