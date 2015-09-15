from django.conf.urls import include, url, patterns
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('liudada.views',
    # Examples:
    # (r'^$', 'liudada.views.home', name='home'),
    # (r'^blog/', include('blog.urls')),

    (r'^admin/', include(admin.site.urls)),
    (r'^hello/$', 'hello'),
    (r'^time/$', 'current_datetime'),
    (r'^time/plus/(\d{1,2})/$', 'hours_ahead'),
    #(r'^book/$', 'book_list'),
    #(r'^search/$', 'search'),
    (r'^contact/$', 'contact'),
)

urlpatterns += patterns('',
    (r'^book/', include('books.urls')),
)