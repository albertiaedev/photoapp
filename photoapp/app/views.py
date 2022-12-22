from django.shortcuts import render

def gallery(request):
    return render(request,'app/gallery.html')

def view_photo(request,pk):
    return render(request,'app/photo.html')

def add_photo(request):
    return render(request,'app/add.html')
