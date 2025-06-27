from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Category, Photo
from .forms import PhotoForm
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
    photo = get_object_or_404(Photo, id=pk)
    context = {'photo':photo}
    return render(request,'app/photo.html',context)

def add_photo(request):
    categories = Category.objects.all()

    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            category_id = request.POST.get('category')
            category_new = request.POST.get('category_new')

            if category_id and category_id != 'None':
                category = get_object_or_404(Category, id=category_id)
            elif category_new:
                category, created = Category.objects.get_or_create(name=category_new)
            else:
                category = None

            photo = form.save(commit=False)
            photo.category = category
            photo.save()
            return redirect('gallery')
    else:
        form = PhotoForm()

    context = {'categories': categories, 'form': form}
    return render(request, 'app/add.html', context)

def delete_photo(request):
    if request.method == 'POST':
        photo_id = request.POST.get('photo_id')
        if photo_id:
            try:
                photo = Photo.objects.get(id=photo_id)
                photo.delete()
                return redirect('gallery')
            except Photo.DoesNotExist:
                return HttpResponse("Photo does not exist.", status=404)

    photo_id = request.GET.get('photo_id')
    if photo_id:
        try:
            photo = Photo.objects.get(id=photo_id)
            return render(request, 'app/delete.html', {'photo': photo})
        except Photo.DoesNotExist:
            return HttpResponse("Photo does not exist.", status=404)

    return redirect('gallery')

def edit_photo(request):
    photo_id = request.GET.get('photo_id')
    photo = get_object_or_404(Photo, id=photo_id)

    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES, instance=photo)
        if form.is_valid():
            form.save()
            return redirect('gallery')
    else:
        form = PhotoForm(instance=photo)

    context = {'form': form, 'photo': photo}
    return render(request, 'app/edit.html', context)