from django.contrib.auth.hashers import make_password, check_password
from django.shortcuts import render

# Create your views here.
from User.models import User



def index(request):
    return render(request, 'base.html')


def register(request):
    if request.method == 'GET':
        return '3'
    else:
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        re_password = request.POST.get('re_password')

        if password == re_password:
            makepassword = make_password(password) #自有加密方法
            user = User()
            user.phone = phone
            user.password = makepassword
            user.save()
            return '3'

def login(request):
    if request.method == 'GET':
        return render(request, 'User/login.html')
    else:
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        user = User.objects.filter(phone=phone)
        if user:
            if check_password(password, user.password):
                request.session['user'] = user
                return 'login seccess'
            else:
                return 'password is error'
        else:
            return 'user does not exist'


def logout(request):
    pass