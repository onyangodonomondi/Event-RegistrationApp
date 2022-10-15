from django.shortcuts import render ,redirect
from . import views
from  .models  import  *
# Create your views here.
def index(request):
    data= Experience.objects.all()

    return render(request, 'user/index.html',{'data':data})

# def experience(request):
#     data= Experience.objects.all()
#     print(data)
#     return render(request, 'user/index.html' , {'data':data})


