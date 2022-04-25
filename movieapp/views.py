from django.shortcuts import render, redirect
from .models import Movie
from .forms import MovieForm
def index(request):
    movie=Movie.objects.all()
    return render(request,'index.html',{'movie_list':movie})
def details(request,id):
    movie=Movie.objects.get(id=id)
    return render(request,'details.html',{'movie':movie})
def add(request):
    if request.method=='POST':
        name=request.POST.get('movie_name')
        desc = request.POST.get('movie_description')
        year=request.POST.get('movie_year')
        img=request.FILES['movie_image']
        movie=Movie(name=name,desc=desc,year=year,img=img)
        movie.save()
        return redirect('/')
    return render(request,'add.html')
def update(request,id):
    movie=Movie.objects.get(id=id)
    form=MovieForm(request.POST or None,request.FILES,instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'edit.html',{'form':form})
def delete(request,id):
    movie = Movie.objects.get(id=id)
    if request.method=='POST':
        movie.delete()
        return redirect('/')
    return render(request, 'delete.html')