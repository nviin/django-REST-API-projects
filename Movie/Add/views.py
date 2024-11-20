from django.shortcuts import render,redirect
from Add.models import movie

def Home(request):
    k = movie.objects.all()
    context = {'movie': k}
    return render(request, 'home.html', context)
    return render(request, 'Home.html')
def Add(request):
    if (request.method == "POST"):
        t = request.POST['t']
        l = request.POST['l']
        y = request.POST['y']
        i = request.FILES['i']
        b = movie.objects.create(title=t, language=l, year=y, poster=i)
        b.save()
        return redirect('Home')
    return render(request, 'Add.html')
def Details(request,p):
    m=movie.objects.get(id=p)
    context={'movie':m}
    return render(request,'details.html',context)
def delete(request,p):
    m=movie.objects.get(id=p)
    m.delete()
    return redirect('Home')
def edit(request,p):
    m=movie.objects.get(id=p)
    if (request.method=="POST"):
        m.title=request.POST['t']
        m.language=request.POST['l']
        m.year=request.POST['y']
        if (request.FILES.get('i') == None):
            m.save()
            return redirect('Home')
        else:
            m.poster = request.FILES.get('i')
    context={'movie':m}
    return render(request,'edit.html',context)


