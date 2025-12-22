from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login

# Create your views here.
def login_view(request):
    """
    https://docs.djangoproject.com/en/6.0/topics/auth/default/#authenticating-users
    """
    # GET -> Visit Page / READ
    # POST -> Save
    if request.method == "GET":
        return render(request, 'user/login.html')
    
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/welcome/')
        else:
            return render(
                request, 
                'user/login.html', 
                {
                    'old_username': username,
                    'login_error': True
                }
            )