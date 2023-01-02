from django.shortcuts import render, redirect
from django.views import View
from .models import Movie
from django.http import HttpResponse
from .forms import MovieForm


# Create your views here.

class Index(View):
    def get(self, request):
        movies = Movie.objects.all()
        print(movies)
        return render(request, 'movieapp/index.html', {'movie_list': movies})


class Details(View):
    def get(self, request, movie_id):
        movie = Movie.objects.get(id=movie_id)
        print(movie)
        return render(request, 'movieapp/detail.html', {'movie': movie})

# class AddMovie(View):
#     def get(self,request):
#         return render(request,'movieapp/add.html')
#     def post(self,request):
#         name = request.POST.get('name','')
#         desc = request.POST.get('desc','')
#         year = request.POST.get('year','')
#         image = request.FILES['image']
#
#         movie = Movie(name=name,desc=desc,year=year,image=image)
#         movie.save()

def addmovie(request):
    if request.method =="POST":
        name = request.POST.get('name','')
        desc = request.POST.get('desc','')
        year = request.POST.get('year','')
        image = request.FILES['image']

        movie = Movie(name=name,desc=desc,year=year,image=image)
        movie.save()
    return render(request,'movieapp/add.html')

def update(request,id):
    movie = Movie.objects.get(id=id)
    form = MovieForm(request.POST or None,instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'movieapp/edit.html',{'form':form,'movie':movie})

def delete(request,id):
    if request.method=="POST":
        movie = Movie.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request,'movieapp/delete.html')