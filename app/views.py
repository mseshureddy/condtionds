from ast import Return
from django.shortcuts import render

# Create your views here.
def condtions(request):
    d={'a': 45}
    return render(request,'ifcondtion.html',d)

def condtions1(request):
    d1={'a':445,'b':85}
    return render(request,'if-else condtion.html',d1)

def condtions2(request):
    d2={'a':10,'b':30,}
    return render(request,'if-elif.html',context=d2)

def condtions3(request):
    d3={'a':10,'b':30,'c':40}
    return render(request,'Nested-if.html',d3)

def condtions4(request):
    d4={'a':'SESHU'}
    return render(request,'forloop.html',d4)
