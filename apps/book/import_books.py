import json
from apps.book.models import Book, Author
from datetime import datetime
from cloudinary.uploader import upload

# Open and read the JSON file
with open('apps/book/books.json', encoding='utf-8') as f:
    books = json.load(f)

for b in books: 
    # date parsing with error handling
    try:
        published_date = datetime.strptime(b['published_date'], '%Y-%m-%d').date()
    except ValueError:
        print(f"Invalid date for the book '{b['title']}': {b['published_date']}. Using 1900-01-01 instead.")
        published_date = datetime(1900, 1, 1).date()

    # Create or get Book
    book, created = Book.objects.get_or_create(
        title=b['title'],
        defaults={
            'description': b.get('description', ''),
            'published_date': published_date,
            'stock': b.get('stock', 1)
        }
    )

    # Upload image only if it's a new book
    if created and b.get('cover_image_url'):
        result = upload(b['cover_image_url'], folder="books")
        book.image = result['public_id']
        book.save()

    # Associate authors
    for a in b.get('authors', []):
        author, _ = Author.objects.get_or_create(
            first_name=a['first_name'],
            last_name=a['last_name'],
            country=a['country']
        )
        book.author.add(author)

    print(f"Imported book: {book.title}")
