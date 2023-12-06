from django.shortcuts import render, redirect
from .models import Category, Photo
from django.db.models import Max
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def gallery(request):
    categories = Category.objects.all()
    photos = Photo.objects.all().order_by('-date_added')
    paginator = Paginator(photos, 2)
    page = request.GET.get('page')
    try:
        photos = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        photos = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        photos = paginator.page(paginator.num_pages)
    context = {'categories':categories,'photos':photos}
    return render(request,'app/gallery.html',context)

def view_photo(request,pk):
    photo = Photo.objects.get(id=pk)
    context = {'photo':photo}
    return render(request,'app/photo.html',context)

def add_photo(request):
    categories = Category.objects.all()

    if request.method == 'POST':
        data = request.POST
        image = request.FILES.get('image')

        if data['category'] != 'None':
            category = Category.objects.get(id=data['category'])
        elif data['category_new'] != '':
            category, created = Category.objects.get_or_create(name=data['category_new'])
        else:
            category: None

        photo = Photo.objects.create(
            category=category,
            description=data['description'],
            image=image,
        )

        return redirect('gallery')

    context = {'categories':categories}
    return render(request,'app/add.html',context)
