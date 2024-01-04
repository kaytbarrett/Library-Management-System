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

from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.contrib.auth.hashers import check_password
from rest_framework.parsers import JSONParser
from django.shortcuts import redirect
from django.http import JsonResponse
from rest_framework.permissions import AllowAny
from django.middleware.csrf import get_token


@api_view(['GET', 'POST'])
@permission_classes([AllowAny]) 
def login_api(request):

    print(f"Request Headers: {request.headers}")

    if request.method == 'GET':
        # Handle GET request to retrieve CSRF token
        csrf_token = get_token(request)
        return JsonResponse({'csrf_token': csrf_token})

    elif request.method == 'POST':
        # Handle POST request for login
        data = request.data
        username = data.get('username')
        password = data.get('password')

        # Authenticate user
        user = authenticate(request, username=username, password=password)

        if user is not None and user.check_password(password):
            # Log the user in
            login(request, user)

            # Generate or get an authentication token
            token, created = Token.objects.get_or_create(user=user)

            # Return token or any other data you need
            user_id = user.id
            return JsonResponse({'success': True, 'user_id': user_id, 'token': token.key}, status=200)
        else:
            return JsonResponse({'error': 'Invalid credentials'}, status=401)
    

class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [AllowAny]

class BookRUDView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [AllowAny]

class UserProfileListCreateView(generics.ListCreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [AllowAny]

class UserProfileRUDView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [AllowAny]

class AuthorListCreateView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [AllowAny]

class AuthorRUDView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [AllowAny]

class PublisherListCreateView(generics.ListCreateAPIView):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer
    permission_classes = [AllowAny]

class PublisherRUDView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer
    permission_classes = [AllowAny]

class GenreListCreateView(generics.ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [AllowAny]

class GenreRUDView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [AllowAny]

class BookCopyListCreateView(generics.ListCreateAPIView):
    queryset = BookCopy.objects.all()
    serializer_class = BookCopySerializer
    permission_classes = [AllowAny]

class BookCopyRUDView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BookCopy.objects.all()
    serializer_class = BookCopySerializer
    permission_classes = [AllowAny]

class CheckoutListCreateView(generics.ListCreateAPIView):
    queryset = Checkout.objects.all()
    serializer_class = CheckoutSerializer
    permission_classes = [AllowAny]

class CheckoutRUDView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Checkout.objects.all()
    serializer_class = CheckoutSerializer
    permission_classes = [AllowAny]