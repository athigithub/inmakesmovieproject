from django.http import HttpResponse
from django.shortcuts import render, redirect

from .models import Movie
from .forms import MovieForm

# Create your views here.

def index(request):
    movie=Movie.objects.all()
    content={'movie_list':movie}
    return render(request,"index.html",content)

def movie_detail(request,movie_id):
    movie=Movie.objects.get(id=movie_id)
    return render(request,"detail.html",{'movie_detail':movie})
def addmovie(request):
    if request.method=="POST":
        moviename=request.POST.get('moviename')
        desc=request.POST.get('description')
        year=request.POST.get('year')
        image=request.FILES['image']
        addmovie=Movie(name=moviename,desc=desc,year=year,img=image)
        addmovie.save()
    return render(request,'add_movie.html')

def update(request,id):
    movie=Movie.objects.get(id=id)
    form=MovieForm(request.POST or None,request.FILES,instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'movie':movie})
def delete(request,id):
    if request.method=="POST":
        movie=Movie.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request,'delete.html')



# def update(request,movie_id):
#     movie=Movie.objects.get(id=movie_id)
#     print(movie_id)
#     form = MovieForm(request.POST or None , request.FILES, instance=movie)
#
#     if form.is_valid():
#         form.save()
#         return redirect('/')
#     return render(request,'edit.html',{'from':form,'movie':movie})

# def movie_detail(request,movie_id):
#     return HttpResponse("this is movie no %s "% movie_id)