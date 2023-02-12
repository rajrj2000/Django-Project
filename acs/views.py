from django.shortcuts import render,redirect
from acs.forms import EnquiryForm

# Create your views here.

def course (request):
    return render (request,'raj.html')

def college(request):
    return render(request,'manju.html')

def sampleForm(request):
    form=EnquiryForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('coursepage')
    return render(request,'sampleform.html',{'data':form})


