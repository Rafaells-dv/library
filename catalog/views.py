from django.views import generic
from django.shortcuts import render
from catalog.models import Book, BookInstance, Author, Genre


# Create your views here.
def index(request):

    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    num_instances_disponiveis = BookInstance.objects.filter(status__exact='d').count

    num_authors = Author.objects.count()

    num_genre = Genre.objects.count()
    num_hp_books = BookInstance.objects.filter(book__title__icontains='Harry').count

    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_disponiveis,
        'num_authors': num_authors,
        'num_genre': num_genre,
        'num_hp_books': num_hp_books,
        'num_visits': num_visits,
    }

    return render(request, 'index.html', context=context)


class BookListView(generic.ListView):
    model = Book
    paginate_by = 10


class BookDetailView(generic.DetailView):
    model = Book


class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 10


class AuthorDetailView(generic.DetailView):
    model = Author
