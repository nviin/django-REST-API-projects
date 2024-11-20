from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from app1.models import CustomUser


def register(request):
        if (request.method == "POST"):
            u = request.POST['u']
            p = request.POST['p']
            cp = request.POST['cp']
            e = request.POST['e']
            f = request.POST['f']
            l = request.POST['l']
            if (p == cp):
                u = CustomUser.objects.create_user(username=u, password=p, email=e, first_name=f, last_name=l)
                u.save()
            else:
                return HttpResponse(request, "PASSWORD SHOULD BE SAME")
                return redirect('book:home')

        return render(request,'register.html')
def user_login(request):
    if(request.method=="POST"):
        u=request.POST['u']
        p=request.POST['p']

        user=authenticate(username=u,password=p)

        if user:
            login(request,user)
            return redirect('app1:home')
        else:
            return HttpResponse("Invalid Credentials")
    return render(request,'login.html')
def user_logout(request):
    logout(request)
    return redirect('app1:login')
