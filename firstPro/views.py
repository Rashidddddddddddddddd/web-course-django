from tokenize import group
from unittest import removeResult

from django.shortcuts import HttpResponse, render, redirect

# djangoning user modelni import qildm
from django.contrib.auth.models import User, Group

from new.models import New
from extra.models import Carusel

def home(request):
    print(request.user.is_superuser)
    news = New.objects.all()[:3]
    carusel = Carusel.objects.all()
    return render(request, 'page/home.html', {'news': news, 'carusel': carusel}) 

def users_view(request):
    users = User.objects.all()
    return render(request, "accounts/users.html", {"users": users})

def update_view(request, pk):
    user = User.objects.get(pk=pk)
    if request.method == 'POST':
        user.username = request.POST.get('username')
        user.email = request.POST.get('email')
        user.save()
        return redirect('users')
    form = UserUpdateForm(initial={'supervisor': user})
    return render(request, 'accounts/update_user.html', {"form": form})



def groups_view(request):
    groups = Group.objects.all()
    return render(request, "accounts/groups.html", {"groups": groups})

