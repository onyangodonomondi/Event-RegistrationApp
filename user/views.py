from django.shortcuts import render ,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from  . forms import UserRegisterForm
# Create your views here.
def index(request):
    return render(request, 'user/index.html')

def login(request):
    return render(request, 'user/login.html')
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('index')
    else:
        form=UserRegisterForm()
    return render(request, 'user/register.html', {'form':form})
def logout(request):
    return render(request, 'user/logout.html')

def profile(request):
    
    return render(request, 'user/profile.html')
def categories(request):
    return render(request, 'user/categories.html')

def resources(request):
    return render(request, 'user/resources.html')
def contact(request):
    return render(request, 'user/contact.html')
    

    

