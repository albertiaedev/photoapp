from django.shortcuts import render
from .models import Category, Photo

def gallery(request):
    categories = Category.objects.all()
    photos = Photo.objects.all()
    context = {'categories':categories,'photos':photos}
    return render(request,'app/gallery.html',context)

def view_photo(request,pk):
    photo = Photo.objects.get(id=pk)
    context = {'photo':photo}
    return render(request,'app/photo.html',context)

def add_photo(request):
    return render(request,'app/add.html')
