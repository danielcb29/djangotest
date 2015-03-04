from django.shortcuts import render,render_to_response
from forms import ContactForm
from django.db.models import Q
from books.models import *
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_protect #Dajngo csrf verification, no book
from django.http import HttpResponse
from books.forms import *
# Create your views here.

def search(request):
    query = request.GET.get('q', '')
    if query:
        qset = (
            Q(title__icontains=query) |
            Q(authors__first_name__icontains=query) |
            Q(authors__last_name__icontains=query)
        )
        results = Book.objects.filter(qset).distinct()
    else:
        results = []
    return render_to_response("books/search.html", {
        "results": results,
        "query": query
    })

def search_new(request):
    errors = []
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            errors.append('Enter a search term.')
        elif len(q) > 20:
            errors.append('Please enter at most 20 characters.')
        else:
            books = Book.objects.filter(title__icontains=q)
            return render(request, 'books/search_results.html',
                {'books': books, 'query': q})
    return render(request, 'books/search_form.html',
        {'errors': errors})


def contact(request):
    errors = []
    if request.method == 'POST':
        if not request.POST.get('subject', ''):
            errors.append('Enter a subject.')
        if not request.POST.get('message', ''):
            errors.append('Enter a message.')
        if request.POST.get('email') and '@' not in request.POST['email']:
            errors.append('Enter a valid e-mail address.')
        if not errors:
            '''send_mail(
                request.POST['subject'],
                request.POST['message'],
                request.POST.get('email', 'noreply@example.com'),
                ['daniel.correa@correounivalle.edu.co'],
            )'''
            return HttpResponseRedirect('/contact/thanks/')
    return render(request, 'books/contact.html', {
        'errors': errors,
        'subject': request.POST.get('subject', ''),
        'message': request.POST.get('message', ''),
        'email': request.POST.get('email', ''),
    })
def display_meta(request):
    values = request.META.items()
    values.sort()
    html = []
    for k, v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))

def thanks(request):
    return HttpResponse("Thanks for sending mail, we are going to send a feedback")
def show_dcbook(request):
    book = Book.objects.get()
    form = BookForm(instance=book)
    return HttpResponse(form)