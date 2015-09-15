from django.shortcuts import render
from django.views.generic import ListView
from books.models import Book

# Create your views here.
def book_list(request):
    books = Book.objects.order_by('title')
    return render(request, 'books/book_list.html', {'books':books})

def search(request):
    errors = []
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            errors.append('Enter a search term.')
        elif len(q) > 20:
            errors.append('Please enter at most 20 characters.')
        else:
            books = Book.objects.filter(title__icontains=q)
            return render(request, 'book_list.html', {'books':books, 'query':q})
    return render(request, 'search_form.html', {'errors':errors})

class BookListView(ListView):
    model = Book
    def head(self, *args, **kargs):
        last_book = self.get_queryset().last_book('publication_date')
        response = HttpResponse('')
        response['Last-Modified'] = last_book.publication_date.strftime('%a, %d %b %Y %H:%M:%s GMT')
        response['books'] = Book.objects.order_by('title')
        return response