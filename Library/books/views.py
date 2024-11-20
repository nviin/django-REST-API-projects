from django.shortcuts import render,redirect
from books.models import Book
from django.contrib.auth.decorators import login_required
from django.db.models import Q
def home(request):
    return render(request,'home.html')

@login_required
def addbooks(request):
    if(request.method=="POST"):
        t=request.POST['t']
        n = request.POST['n']
        l = request.POST['l']
        p = request.POST['p']
        pa = request.POST['pa']
        c = request.FILES['c']
        f = request.FILES['f']
        b=Book.objects.create(title=t,author=n,language=l,price=p,pages=pa,cover=c,pdf=f)
        b.save()
    return render(request,'addbooks.html')

@login_required
def viewbooks(request):
    from books.models import Book
    k=Book.objects.all()  #read all records from the table
    context={'book':k}  #passes data from views to html file,Context is dictionary type.
    return render(request,'viewbooks.html',context)

def detail(request,p):
    b=Book.objects.get(id=p)#reads a particular record from table book
    context={'book':b}
    return render(request,'detail.html',context)
def edit (request,p):
        b = Book.objects.get(id=p)
        if (request.method == "POST"):  # After submitting form
            b.title = request.POST['t']
            b.author = request.POST['n']
            b.price = request.POST['p']
            b.page = request.POST['pa']
            b.language = request.POST['l']
            if (request.FILES.get('c') == None):
                b.save()
            else:
                b.cover = request.FILES.get('c')
            if (request.FILES.get('f') == None):
                b.save()
            else:
                b.pdf = request.FILES.get('f')

            b.save()
            return redirect('books:viewbooks')

        context = {'book': b}
        return render(request, 'edit.html', context)
def delete(request,p):
    b=Book.objects.get(id=p)
    b.delete()
    return redirect('books:viewbooks')
def search(request):

    if (request.method=="POST"):
        b = None
        query = ""
        query=request.POST['q']
        if query:
            b=Book.objects.filter(Q(title__icontains=query)  |  Q(author__icontains=query))
    return render(request,'search.html',{'books':b, 'query':query})


