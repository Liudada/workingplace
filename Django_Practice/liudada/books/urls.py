from django.conf.urls import include, url, patterns
from books.views import BookListView

urlpatterns = patterns('books.views',
    (r'^$', 'book_list'),
    (r'^search$', 'search'),
)