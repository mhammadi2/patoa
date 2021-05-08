from django.shortcuts import render, redirect
from .forms import LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.http import HttpResponse

def home_view(request):
    return render(request, 'home.html', {})

def logout_view(request):
    logout(request)
    return redirect('home')

def login_view(request):
    error_message = None
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                if request.GET.get('next'):
                    return redirect(request.GET.get('next'))
                else:
                    return redirect('home')

            else:
                error_message = 'Ups.Something went wrong...'
                
    return render(request, 'login.html', {'form':form, 'error_message': error_message})


def register_view(request): #If POST, then register user and redirect, otherwise render template
    if request.method == 'POST':
        # Get form values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        # Check if passwords match
        if password == password2:
            # Check for new username
            if User.objects.filter(username=username).exists():
                messages.error(request, 'That username is taken')
                return redirect('signin')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'That email is being used')
                    return redirect('signin')
                else:
                    # Looks good
                    user = User.objects.create_user(
                        username=username, 
                        password=password, 
                        email=email,
                        first_name=first_name,
                        last_name=last_name
                    )
                    #Login after register
                    #auth.login(request, user)
                    #messages.success(request, 'You are now logged in')
                    #return redirect('index')
                    
                    #redirect to login page to login for first time
                    user.save()
                    messages.success(request, 'You are now registered and can log in')
                    return redirect('login')
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('signin')
    else:
        return render(request, 'signin.html')

