from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Feature


# Create your views here.
def index(request):
    features = Feature.objects.all()
    return render(request, 'index.html', {'featureloop': features})

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        # Validation
        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email already used!')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'User already added')
                return redirect('register')
            else:
                user = User.objects.create_user(username= username, email = email, password = password)
                user.save()
                return redirect('login')
        else:
            messages.info(request, 'Password is not same')
            return redirect('register')

    else:
        return render(request, 'register.html')

def counter(request):
    text = request.POST['text']
    words_amount = len(text.split())
    return render(request, 'counter.html', {'amount': words_amount})