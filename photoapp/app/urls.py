from django.urls import path
from . import views

urlpatterns = [
    path('',views.gallery,name='gallery'),
    path('photo/<str:pk>/',views.view_photo,name='photo'),
    path('add/',views.add_photo,name='add'),
    path('delete/',views.delete_photo,name='delete'),
    path('edit/',views.edit_photo,name='edit'),
]
