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
    


    return render(request, 'user/index.html',{'data':data,'data1':data1, 'data2':data2, 'data3':data3, 'form':form, 'submitted':submitted})

   
def categoryPage(request, slug):

    category = Category.objects.get(slug=slug)
    images = Image.objects.filter(category=category).order_by('-date_created')[:6]
    for x in images:
        x.shortDescription = x.description[:130]

    context = {}
    context['images'] = images
    context['category'] = category

    return render(request, 'user/portfolio.html', context)