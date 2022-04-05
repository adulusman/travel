from django.shortcuts import render

from .models import Place, Team


# Create your views here.

def demo(request):
    obj=Place.objects.all()
    obj1=Team.objects.all()
    return render(request, 'index.html',{'result':obj,
                                         'result2':obj1})
def dem(request):
    return render(request,'home.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')

def addition(request):
    x=int(request.GET['num1'])
    y=int(request.GET['num2'])
    res=x+y
    return render(request,'result.html',{'addit':res})
