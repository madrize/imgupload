from django.shortcuts import render_to_response
from django.contrib.auth import logout,login,authenticate
from forms import *
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm

def mylogin(request,
            logged_url='/',
            template='reg/login.html',
            success_page='/',
            error_page='/'):
    if request.user.is_authenticated():
        return HttpResponseRedirect(logged_url)
    
    if request.method == 'POST':
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        user = authenticate(username=username,password=password)
        form = AuthenticationForm(request.POST)
        
        if user is not None:
            login(request,user)
            return HttpResponseRedirect(success_page)
    else:
        form = AuthenticationForm()
    
    return render_to_response(template,
                              {'form' : form },
                              context_instance=RequestContext(request)) 


def register(request,template="reg/register.html"):
    if request.user.is_authenticated():
        return HttpResponseRedirect("/logged-in/")
    
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1'],
                email=form.cleaned_data['email']
            )
            return HttpResponseRedirect("/")
    else:
        form = RegistrationForm()
    
    return render_to_response(    template,
                                {"form":form},
                                context_instance=RequestContext(request))

def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/')