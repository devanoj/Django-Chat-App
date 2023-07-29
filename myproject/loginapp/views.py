from django.shortcuts import render

import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth

from django.shortcuts import render, redirect

# loginapp/views.py

from django.shortcuts import render, redirect

def login_view(request):
    # Set is_login_successful to False by default
    is_login_successful = False

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username == "admin":
            is_login_successful = True

    if is_login_successful:
        # Redirect to the success page with the username as a parameter
        return redirect('login_success', username=username)
    else:
        # Handle failed login (e.g., display an error message)
        return render(request, 'loginapp/login.html', {'error_message': 'Invalid credentials'})

    return render(request, 'loginapp/login.html')





def signup_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
    
    return render(request, 'loginapp/signup.html')


def success_view(request, username):
    return render(request, 'loginapp/success.html', {'username': username})

