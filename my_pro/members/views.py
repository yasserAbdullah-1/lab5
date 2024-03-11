from  django.urls import reverse
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django import forms

class person:
    def __init__(self,name,password):
        self.username=name
        self.password=password
        
   
class NewTaskForm(forms.Form):
    username=forms.CharField(label='username')
    password=forms.CharField(label='password')
people=[]    
def index(request):
    return render(request,'members/index.html',{'people':people})    

def add(request):
    
    if request.mehthod=="POST":
        np=person() 
        form=NewTaskForm(request.POST)
        if form.is_valid():
            np.username=form.cleaned_data['username']
            np.password=form.cleaned_data['password']
        
            people.append(np)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request,'members/add.html',{"form":NewTaskForm()}) 
    return render(request,'members/add.html',{"form":NewTaskForm()}) 
  