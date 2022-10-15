from django.shortcuts import render ,redirect
from . import views
from  .models  import  *
# Create your views here.
def index(request):
    data= Experience.objects.all()
    data1= Education.objects.all()

    return render(request, 'user/index.html',{'data':data},{'data1':data1})

# def experience(request):
#     data= Experience.objects.all()
#     print(data)
#     return render(request, 'user/index.html' , {'data':data})


