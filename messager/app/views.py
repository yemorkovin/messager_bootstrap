from django.contrib.auth.hashers import make_password, check_password
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
def index(request):
    return render(request, 'index.html')

def ajaxReg(request):
    if request.method == 'POST':
        login = request.POST['login']
        password = request.POST['password']
        if User.objects.filter(login=login).exists():
            return HttpResponse('1')
        if len(login) <= 5:
            return HttpResponse('2')
        if len(password) <= 5:
            return HttpResponse('3')
        user = User()
        user.login = login
        user.password = make_password(password)
        user.save()
        return HttpResponse('4')

def ajaxAuth(request):
    if request.method == 'POST':
        login = request.POST['login']
        password = request.POST['password']
        if User.objects.filter(login=login).exists():
            user = User.objects.filter(login=login).first()
            if check_password(password, user.password):
                request.session['user'] = login
                return HttpResponse('1')
            else:
                return HttpResponse('2')
        else:
            return HttpResponse('3')


def lk(request):
    if not 'user' in request.session:
        return redirect('/')
    if request.method == 'POST':
        #обработка формы редактирования данных
        name = request.POST['name']
        login = request.POST['login']
        new_password = request.POST['new_password']
        old_password = request.POST['old_password']
        avatar = ''
        if 'image' in request.FILES:
            if request.FILES['image']:
                image = request.FILES['image']
                fs = FileSystemStorage()
                fs.save('users_avatar/'+image.name, image)
                avatar = 'users_avatar/'+image.name
        user = User.objects.filter(login=request.session['user']).first()
        user.name = name
        user.login = login
        if check_password(old_password, user.password):
            user.password = make_password(new_password)
        if avatar != '':
            user.avatar = avatar
        user.save()
    user = User.objects.filter(login=request.session['user']).first()
    return render(request, 'lk/profile.html', {'user': user})


def logout(request):
    if 'user' in request.session:
        del request.session['user']
    return redirect('/lk')

