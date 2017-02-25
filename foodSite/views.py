from foodSite.forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response,render
from django.http import HttpResponseRedirect
from django.template import RequestContext
from foodSite.models import *

@csrf_protect
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            stat = form.cleaned_data['choice_field']
            if stat=="Costumer" : 
                status="C"
                C=Customer(name=form.cleaned_data['first_name'],passwd=form.cleaned_data['password1'],email=form.cleaned_data['email'],contact=form.cleaned_data['username'])
                C.save()
            else : 
                status="R"
                R=Restaurant(name=form.cleaned_data['first_name'],passwd=form.cleaned_data['password1'],email=form.cleaned_data['email'],contact=form.cleaned_data['username'])
                R.save() 

            user = User.objects.create_user(
            first_name=form.cleaned_data['first_name'],
            last_name=status,
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password1'],
            email=form.cleaned_data['email']
            )
            return HttpResponseRedirect('success/')
    else:
        form = RegistrationForm()
 
    return render(request,
    'registration/register.html',
    {'form': form}
    )
 
def register_success(request):
    return render_to_response(
    'registration/success.html',{'user':request.user}
    )
 
def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')
 
@login_required
def home(request):
    return render_to_response(
    'home.html',
    { 'user': request.user }
    )