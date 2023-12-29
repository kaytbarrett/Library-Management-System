# your_app/management/commands/seed_data.py
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from libraryApp.models import Book, UserProfile, Publisher, Genre, Author, BookCopy, Checkout

class Command(BaseCommand):
    help = 'Seed database with initial data'

    def add_arguments(self, parser):
        parser.add_argument('--users', type=int, default=3, help='Number of users to create')
        parser.add_argument('--books', type=int, default=14, help='Number of books to create')

    def handle(self, *args, **options):
        num_users = options['users']
        num_books = options['books']

        for user_num in range(1, num_users + 1):
            username = f'user{user_num}'
            raw_password = f'password{user_num}'  # Set password based on user number
            hashed_password = make_password(raw_password)  # Hash the password
            email = f'User{user_num}@example.com'  # Set a dummy email for now
            phone_number = f'555-555-000{user_num}'  # Set a dummy phone number for now
            name = f'User {user_num} Name'  # Set a dummy name for now

            user = User.objects.create(username=username, password=hashed_password, email=email)
            UserProfile.objects.create(user=user, bio=f'Bio for {username}', phone_number=phone_number, name=name)

        # Create books with cover images
        book_data = [
            {'title': 'To Kill a Mockingbird', 'author': 'Harper Lee', 'publication_date': '1960-07-11', 'price': 12.99, 'cover_image': 'https://m.media-amazon.com/images/I/81JYG8sqRsL._SL1500_.jpg'},
            {'title': 'The Great Gatsby', 'author': 'F. Scott Fitzgerald', 'publication_date': '1925-04-10', 'price': 14.99, 'cover_image': 'https://m.media-amazon.com/images/I/71F7v5uTFHL._SL1500_.jpg'},
            {'title': '1984', 'author': 'George Orwell', 'publication_date': '1949-06-08', 'price': 11.99, 'cover_image': 'https://m.media-amazon.com/images/I/517OS8CQc0L._SL1202_.jpg'},
            {'title': 'The Catcher in the Rye', 'author': 'J.D. Salinger', 'publication_date': '1951-07-16', 'price': 10.99, 'cover_image': 'https://m.media-amazon.com/images/I/91HPG31dTwL._SL1500_.jpg'},
            {'title': 'Lord of the Flies', 'author': 'William Golding', 'publication_date': '1954-09-17', 'price': 13.99, 'cover_image': 'https://m.media-amazon.com/images/I/81t-Qi4X6HL._SL1500_.jpg'},
            {'title': 'The Hobbit', 'author': 'J.R.R. Tolkien', 'publication_date': '1937-09-21', 'price': 15.99, 'cover_image': 'https://m.media-amazon.com/images/I/71553UI53YL._SL1500_.jpg'},
            {'title': 'Pride and Prejudice', 'author': 'Jane Austen', 'publication_date': '1813-01-28', 'price': 14.99, 'cover_image': 'https://m.media-amazon.com/images/I/61vrbLFc8oL._SL1200_.jpg'},
            {'title': 'Harry Potter and the Philosopher\'s Stone', 'author': 'J.K. Rowling', 'publication_date': '1997-06-26', 'price': 17.99},
            {'title': 'Harry Potter and the Chamber of Secrets', 'author': 'J.K. Rowling', 'publication_date': '1998-07-02', 'price': 18.99},
            {'title': 'Harry Potter and the Prisoner of Azkaban', 'author': 'J.K. Rowling', 'publication_date': '1999-07-08', 'price': 19.99},
            {'title': 'Harry Potter and the Goblet of Fire', 'author': 'J.K. Rowling', 'publication_date': '2000-07-08', 'price': 21.99},
            {'title': 'Harry Potter and the Order of the Phoenix', 'author': 'J.K. Rowling', 'publication_date': '2003-06-21', 'price': 22.99},
            {'title': 'Harry Potter and the Half-Blood Prince', 'author': 'J.K. Rowling', 'publication_date': '2005-07-16', 'price': 23.99},
            {'title': 'Harry Potter and the Deathly Hallows', 'author': 'J.K. Rowling', 'publication_date': '2007-07-21', 'price': 24.99},
        ]

        for book_info in book_data:
            author, _ = Author.objects.get_or_create(name=book_info['author'])
            publisher, _ = Publisher.objects.get_or_create(name='Publisher Name')  # Add a default publisher
            genre, _ = Genre.objects.get_or_create(name='Genre Name')  # Add a default genre

            Book.objects.create(
                title=book_info['title'],
                author=author,
                publication_date=book_info['publication_date'],
                price=book_info['price'],
                cover_image=book_info.get('cover_image', None),
                genre=genre,
                publisher=publisher
            )

        self.stdout.write(self.style.SUCCESS('Data seeded successfully!'))