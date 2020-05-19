from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib.auth import login, authenticate, logout
from myuser.forms import LoginForm, SignupForm
from myuser.models import MyUser
from django.contrib.auth.decorators import login_required
from customuser.settings import AUTH_USER_MODEL


@login_required
def index(request):
    data = MyUser.objects.all()
    return render(request, 'index.html', {
        "data": data, "auth_user": AUTH_USER_MODEL
    })


def loginview(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request, username=data['username'], password=data['password']
            )
            if user:
                login(request, user)
            return HttpResponseRedirect(
                request.GET.get('next', reverse('homepage'))
            )
    form = LoginForm()
    return render(request, 'genericform.html', {'form': form})


def logoutview(request):
    logout(request)
    return HttpResponseRedirect(reverse('homepage'))


def adduser(request):
    html = "signup.html"
    form = SignupForm()

    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_user = MyUser.objects.create_user(
                username=data['username'],
                display_name=data['display_name'],
                password=data['password1'],
            )
        new_user.save()
        login(request, new_user)
        return HttpResponseRedirect(reverse('homepage'))
    form = SignupForm()
    return render(request, html, {'form': form})
