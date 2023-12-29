"""
URL configuration for libraryServer project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from libraryApp.views import (BookListCreateView, BookRUDView, 
                              UserProfileListCreateView, UserProfileRUDView, 
                              AuthorListCreateView, AuthorRUDView,
                              PublisherListCreateView, PublisherRUDView,
                              GenreListCreateView, GenreRUDView,
                              BookCopyListCreateView, BookCopyRUDView,
                              CheckoutListCreateView, CheckoutRUDView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/books/', BookListCreateView.as_view(), name="book-list"),
    path('api/books/<int:pk>/', BookRUDView.as_view(), name="book-detail"),
    path('api/users/', UserProfileListCreateView.as_view(), name="userprofile-list"),
    path('api/users/<int:pk>/', UserProfileRUDView.as_view(), name="userprofile-detail"),
    path('api/authors/', AuthorListCreateView.as_view(), name="author-list"),
    path('api/authors/<int:pk>/', AuthorRUDView.as_view(), name="author-detail"),
    path('api/publishers/', PublisherListCreateView.as_view(), name="publisher-list"),
    path('api/publishers/<int:pk>/', PublisherRUDView.as_view(), name="publisher-detail"),
    path('api/genres/', GenreListCreateView.as_view(), name="genre-list"),
    path('api/genres/<int:pk>/', GenreRUDView.as_view(), name="genre-detail"),
    path('api/bookcopy/', BookCopyListCreateView.as_view(), name="bookcopy-list"),
    path('api/bookcopy/<int:pk>/', BookCopyRUDView.as_view(), name="bookcopy-detail"),
    path('api/checkout/', CheckoutListCreateView.as_view(), name="checkout-list"),
    path('api/checkout/<int:pk>/', CheckoutRUDView.as_view(), name="checkout-detail"),
]

