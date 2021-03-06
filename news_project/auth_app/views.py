from django.shortcuts import render_to_response
from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse #direct browser to diff url
from django.contrib import auth #confirm login jobs
from django.core.context_processors import csrf #cross side request
from django.contrib.auth.forms import UserCreationForm
from form import MyRegistrationForm
# Create your views here.
def login(request):
    c={}
    c.update(csrf(request))
    return render_to_response('login.html', c )

def auth_view(request):
    username = request.POST.get('username','')
    password = request.POST.get('password','')
    user = auth.authenticate(username=username,password=password)

    if user is not None:
        auth.login(request,user)


        return HttpResponseRedirect('/main_page',request)
    else:
        return HttpResponseRedirect('/accounts/invalid')

def loggedin(request):
    return render_to_response('loggedin.html',{'full_name':request.user.username})

def invalid_login(request):
    return render_to_response('invalid_login.html')

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/main_page',request)

def register_usr(request):
    if request.method=='POST':
            form = MyRegistrationForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/accounts/register_success')
            else:

                return render_to_response('invalid_login.html')
    args= {}
    args.update(csrf(request))

    args['form'] = MyRegistrationForm()
    return render_to_response('register.html',args)

def register_success(request):
    return render_to_response('register_success.html')
