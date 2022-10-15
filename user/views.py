from django.shortcuts import render ,redirect
from . import views
from  .models  import  *
# Create your views here.
def index(request):
    data= Experience.objects.all()
    data1= Education.objects.all()
    data2= skills.objects.all()

    return render(request, 'user/index.html',{'data':data,'data1':data1, 'data2':data2 })
   
