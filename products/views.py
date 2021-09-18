from django.shortcuts import render
from . models import place,blog
# Create your views here.
def home(request):
    obj=place.objects.all()
    obj1=blog.objects.all()
    return render(request,'index.html',{'result':obj,'results':obj1})