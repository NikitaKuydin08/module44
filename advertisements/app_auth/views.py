from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout

#vxod
def login_view(request):
    redirect_url = reverse("profile")
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect(redirect_url)
        else:
            return render(request, 'app_auth/login.html')
        
    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
        return redirect(redirect_url)
    return render(request, 'app_auth/login.html')

#profeli
def profile_view(request):
    return render(request, 'app_auth/profile.html')

#vixod
def logout_view(request):
    logout(request)
    return redirect(reverse("login"))