from rest_framework import serializers
from libraryApp.models import Book, UserProfile, Author, Publisher, Genre, BookCopy, Checkout

class BookSerializer(serializers.ModelSerializer):
     class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'publication_date', 'price', 'cover_image', 'genre', 'publisher']

        # Add serializers for related fields
        author = serializers.CharField(source='author.name')
        genre = serializers.CharField(source='genre.name')
        publisher = serializers.CharField(source='publisher.name')

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['user', 'name', 'bio', 'email', 'phone_number']

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['name', 'biography', 'birthdate', 'nationality']

class PublisherSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Publisher
        fields = ['name', 'address', 'contact_email', 'contact_phone']

class GenreSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Genre
        fields = ['name']

class BookCopySerializer(serializers.ModelSerializer):
    class Meta:
        model = BookCopy
        fields = ['book', 'copy_number', 'condition', 'location', 'is_available']

class CheckoutSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Checkout
        fields = ['user', 'book_copy', 'checkout_date', 'return_date']
