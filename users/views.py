from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from users.forms import CreateUserForm, UpdateProfileForm
from django.contrib.auth.decorators import login_required


# Create your views here.
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('feed')
        else:
            return render(request, 'users/login.html', {'error': 'Usuario o contraseña inválidos'})

    return render(request, 'users/login.html')


def register_view(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'users/login.html')
    return render(request, 'users/register.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')


@login_required(login_url="login")
def profile_view(request):
    profile = request.user.profile
    if request.method == 'POST':
        form = UpdateProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = UpdateProfileForm()

    return render(request, 'users/profile.html', {
            'profile': profile,
            'user': request.user,
            'form': form
        }
    )
