from django.contrib import auth, messages
from django.contrib.auth.models import User

from django.shortcuts import redirect, render

from .forms import detailsform
from .models import Details


def home(request):
    return render(request, "first.html")



def login(request):
    if request.method == "POST":

        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:

            auth.login(request, user)
            return redirect('/')

        else:
            messages.info(request, "Wrong input")
            return redirect("login")

    return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')


def register(request):
    is_registered = False

    if request.method == "POST":

        username = request.POST['username']
        password = request.POST['password']
        copassword = request.POST['copassword']

        if password == copassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "username already taken")
                return redirect("register")
            else:
                user = User.objects.create_user(username=username, password=password)
                user.save();
                is_registered = True
                return redirect("login")
        else:
            messages.info(request, "password not matching")
            return redirect("register")

    return render(request, 'register.html', {'is_registered': is_registered})


def details(request):

    form = Details.objects.all()

    return render(request, "details.html",{"form":form})


def enquiry(request):

    form = detailsform(request.POST or None)

    if form.is_valid():
        form.save()

        return redirect("details")

    return render(request, 'enquiry.html')

