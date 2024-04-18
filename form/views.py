from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from . models import Babiesform,Payment,Category_stay
from . forms import BabiesFormForm
# Create your views here.
def sitterform(request):
   babies_informations =Babiesform.objects.all()
   context={'babies_informations':'babies_informations'}
   template=loader.get_template('sitterform.html')
   return HttpResponse(template.render(context))
  
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

def read(request,id):
    babies_informations =Babiesform.objects.get(id=id)
    context={'babies_informations':'babies_informations'}
    template=loader.get_template('read.html')
    return HttpResponse(template.render(context))