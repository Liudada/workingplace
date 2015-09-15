from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.mail import send_mail
from django.shortcuts import render
from django.template import RequestContext
from books.models import Book
from liudada.forms import ContactForm
import datetime

def hello(request):
    values = request.META.items()
    html = []
    for k,v in values:
        html.append("<tr><td>%s</td><td>%s</td></tr>" % (k,v))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))

def custom_proc(request):
    return {
        'app': 'My app',
        'user': '<b>' + str(request.user) + '</b>',
        'ip_address': '<b>' + str(request.META['REMOTE_ADDR']) + '</b>',
    }

def current_datetime(request):
    now = datetime.datetime.now()
    return render(request, 'current_datetime.html', context_instance=RequestContext(request,processors=[custom_proc]))

def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    return render(request, 'hours_ahead.html', {'hour_offset':offset, 'next_time':dt})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email', 'liudada2013@outlook.com'),
                ['liujs2013@gmail.com'],
            )
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form = ContactForm(initial={'subject':'I love django'})
    return render(request, 'contact_form.html', {'form': form})