from django.shortcuts import render
from .models import Category, Photo

def gallery(request):
    categories = Category.objects.all()
    context = {'categories':categories}
    return render(request,'app/gallery.html',context)

def view_photo(request,pk):
    return render(request,'app/photo.html')

def add_photo(request):
    return render(request,'app/add.html')
