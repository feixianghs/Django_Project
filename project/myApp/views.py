from django.http import HttpResponse, response
from django.shortcuts import render, redirect


# Create your views here.
def index(request):
    # fromPath=request.POST.get('from')
    name=request.session.get('username')
    context={'user':name}
    return render(request,'index.html',context)


def login(request):
    if request.method=='GET':
        fromPath=request.GET.get('from')
        return render(request, 'login.html',{'fromPath':fromPath})
    elif request.method=='':
        return render(request, 'login.html')
    else:
        username=request.POST.get('username')
        password=request.POST.get('password')
        fromPath = request.GET.get('from')
        if username=='feixianghs' and password=='123456':
            fromPath='/'+fromPath+'/'
            request.session['username']=username
            response=redirect(fromPath)
            return response
        else:
            urlpath='/login/?from='+fromPath
            return redirect(urlpath)



def home(request):
    # fromPath = request.POST.get('from')
    name = request.session.get('username')
    context = {'user': name}
    return render(request, 'home.html', context)


from django.contrib.auth import logout
def quite(request):
    logout(request)
    urlPath = "/" + request.GET.get("to") + "/"
    return redirect(urlPath)


def upload(request):
    if request.method=='GET':
        return  render(request,'upload.html')
    return None