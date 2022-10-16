from django.shortcuts import render ,redirect
from django.http import HttpResponse
from . import views
from  .models  import  *
from .form import ContactForm
# Create your views here.
def index(request):
    submitted=False

    form=ContactForm
    if request.method == 'POST':
        
        form=ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form=ContactForm()
        if 'submitted' in request.GET:
            submitted=True
        
    data= Experience.objects.all()
    data1= Education.objects.all()
    data2= skill.objects.all()
    data3= Blog.objects.all()
    data4= portfolio.objects.all()

    return render(request, 'user/index.html',{'data':data,'data1':data1, 'data2':data2, 'data3':data3, 'data4':data4 ,'form':form, 'submitted':submitted})


   
