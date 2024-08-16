from django.shortcuts import render
from .forms import *
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail
from django.contrib.auth import authenticate,login
from django.urls import reverse
# Create your views here.

def register(request):
    EUFO = UserForm()
    EPFO = ProfileForm()
    d = {'EUFO': EUFO, 'EPFO': EPFO}
    if request.method == 'POST' and request.FILES:
        UFDO = UserForm(request.POST)
        PFDO = ProfileForm(request.POST, request.FILES)
        if UFDO.is_valid() and PFDO.is_valid():
            pw = UFDO.cleaned_data.get('password')
            MUFDO = UFDO.save(commit=False)
            MUFDO.set_password(pw)
            MUFDO.save()
            MPFDO = PFDO.save(commit=False)
            MPFDO.username=MUFDO
            MPFDO.save()
            message = f"Hello {UFDO.cleaned_data.get('first_name')}\n \t Your Registration against our application is successfully Done with username:{UFDO.cleaned_data.get('username')} \n\n \t\t Thanks & regards \n \t\tTeam"
            email = UFDO.cleaned_data.get('email')
            # send_mail(
            #     'Registration Successfull',
            #     message,
            #     'likith.qsp@gmail.com',
            #     [email],
            #     fail_silently=False
            # )
            return HttpResponseRedirect(reverse('user_login'))
        return HttpResponse('Invalid Data')
    return render(request, 'register.html', d)


def user_login(request):
    if request.method == 'POST':
        un = request.POST.get('un')
        pw = request.POST.get('pw')
        AUO = authenticate(username=un, password=pw)
        if AUO:
            login(request, AUO)
            request.session['username'] = un
            return HttpResponseRedirect(reverse('home'))
        return HttpResponse('Invalid Credentials')
    return render(request, 'user_login.html')

def home(request):
    un = request.session.get('username')
    if un:
        UO = User.objects.get(username=un)
        d = {'UO': UO}
        return render(request, 'home.html', d)
    return render(request, 'home.html')