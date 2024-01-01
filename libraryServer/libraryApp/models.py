from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=True)
    bio = models.TextField(blank=True)
    email = models.EmailField(default='default@example.com')
    phone_number = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.user.username

class Publisher(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField(blank=True)
    contact_email = models.EmailField(blank=True)
    contact_phone = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.name

class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Author(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    biography = models.TextField(blank=True)
    birthdate = models.DateField(null=True, blank=True)
    nationality = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name

class Book(models.Model): 
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publication_date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    cover_image = models.URLField(blank=True, null=True)
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True, blank=True)
    publisher = models.ForeignKey(Publisher, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title

class BookCopy(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    copy_number = models.CharField(max_length=50)
    condition = models.CharField(max_length=100, blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.book.title} - Copy {self.copy_number}"

class Checkout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book_copy = models.ForeignKey(BookCopy, on_delete=models.CASCADE)
    checkout_date = models.DateField()
    return_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.book_copy.book.title}"

    def get_checkout_duration(self):
        if self.checkout_date and self.return_date:
            return self.return_date - self.checkout_date
        return None