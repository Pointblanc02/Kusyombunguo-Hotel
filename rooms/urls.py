from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('about.html', views.about, name="about"),
    path('blog.html', views.blog, name="blog"),
    path('contact.html', views.contact, name="contact"),
    path('gallery.html', views.gallery, name="gallery"),
    path('room.html', views.room, name="room"),
    path('book_now/', views.book_now, name="book_now"),
    # path('viewdata/', views.view, name="view"),
    # path('home.html', views.home, name="home"),
    # path('insert/' views.insert, name="insert"),
    #path('view/' views.view, name="view"),
]

