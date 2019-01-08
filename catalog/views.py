from django.shortcuts import render
from django.views import generic
from catalog.models import Book, Author, BookInstance, Genre

def index(request):
    """View function for home page of site"""

    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    # The 'all()' is implied by default
    num_authors = Author.objects.count()

    # Books containing 'the'
    num_books_containing_the = Book.objects.filter(title__icontains='the').count()

    context = {
      'num_books': num_books,
      'num_instances': num_instances,
      'num_instances_available': num_instances_available,
      'num_authors': num_authors,
      'num_books_containing_the': num_books_containing_the,
    }

    return render(request, 'index.html', context=context)

class BookListView(generic.ListView):
    model = Book
    paginate_by = 10

class BookDetailView(generic.DetailView):
    model = Book
