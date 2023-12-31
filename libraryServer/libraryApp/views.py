from django.shortcuts import render
from rest_framework import generics
from libraryApp.models import Book, UserProfile, Author, Publisher, Genre, BookCopy, Checkout
from .serializers import (
    BookSerializer, 
    UserProfileSerializer, 
    AuthorSerializer, 
    PublisherSerializer, 
    GenreSerializer, 
    BookCopySerializer,
    CheckoutSerializer)

# Create your views here.

class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookRUDView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class UserProfileListCreateView(generics.ListCreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class UserProfileRUDView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class AuthorListCreateView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class AuthorRUDView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class PublisherListCreateView(generics.ListCreateAPIView):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer

class PublisherRUDView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer

class GenreListCreateView(generics.ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

class GenreRUDView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

class BookCopyListCreateView(generics.ListCreateAPIView):
    queryset = BookCopy.objects.all()
    serializer_class = BookCopySerializer

class BookCopyRUDView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BookCopy.objects.all()
    serializer_class = BookCopySerializer

class CheckoutListCreateView(generics.ListCreateAPIView):
    queryset = Checkout.objects.all()
    serializer_class = CheckoutSerializer

class CheckoutRUDView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Checkout.objects.all()
    serializer_class = CheckoutSerializer