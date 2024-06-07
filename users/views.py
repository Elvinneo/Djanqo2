from django.shortcuts import render, redirect, get_object_or_404
from .models import Userss
from .forms import UserForm





def home(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    
    else:
        form = UserForm()
    profiles = Userss.objects.all()
    return render(request, 'main.html', {'form': form, 'profiles': profiles})

def profiles(request):
    users=Userss.objects.all()
    return render(request,'list.html', {'users': users})







