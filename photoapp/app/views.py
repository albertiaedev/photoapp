from django.shortcuts import render
from .models import Category, Photo

def gallery(request):
    categories = Category.objects.all()
    photos = Photo.objects.all()
    context = {'categories':categories,'photos':photos}
    return render(request,'app/gallery.html',context)

def view_photo(request,pk):
    return render(request,'app/photo.html')

def add_photo(request):
    return render(request,'app/add.html')
