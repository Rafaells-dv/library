from django.shortcuts import render
from catalog.models import Book, BookInstance, Author, Genre


# Create your views here.
def index(request):

    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    num_instances_disponiveis = BookInstance.objects.filter(status__exact='d').count

    num_authors = Author.objects.count()

    num_genre = Genre.objects.count()
    num_hp_books = BookInstance.objects.filter(book__title__icontains='Harry Potter').count
    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_disponiveis,
        'num_authors': num_authors,
        'num_genre': num_genre,
        'num_hp_books': num_hp_books,
    }

    return render(request, 'index.html', context=context)