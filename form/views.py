from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from . models import Babiesform,Payment,Category_stay
from . forms import BabiesFormForm
from django.contrib import messages
from django.contrib.auth.models import User ,auth
# Create your views here.
def sitterform(request):
   babies =Babiesform.objects.all()
   return render(request,'sitterform.html',{'babies':babies})
  
def add(request):
   if request.method == 'POST':
   
      form = BabiesFormForm(request.POST)
      
      if form.is_valid():
         form.save()
         print(form)
         return redirect('/')
   else:
      form = BabiesFormForm()
   return render(request,'add.html',{'form':form})


def read(request,id):
    babies_informations =Babiesform.objects.get(id=id)
    return render(request,'read.html',{'babies_informations':babies_informations})


def edit(request,id):
   each = get_object_or_404(Babiesform,id=id)
   if request.method == 'POST':
      form = BabiesFormForm(request.POST,instance=each)
      if form.is_valid():
         form.save()
         return redirect('/')
   else:
      form = BabiesFormForm(instance=each)
   return render(request,'edit.html',{'form':form})

def login(request):
    if request.method == 'POST':
       username = request.POST['username']
       password = request.POST['password']
       user = auth.authenticate(username=username,password=password)
       if user is not None:
           auth.login(request,user)
           return redirect('/')
       else:
           messages.info(request,'Invalid username or password')
           return redirect('/')
    else: 
        return render( request,'login.html',)

    

def logout(request):
      auth.logout(request)
      return redirect('/')








    