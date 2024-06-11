from django.shortcuts import render
from booksandauthors import models as m
from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse, HttpResponseNotFound
# Create your views here.


def add_author(request):
    if request.method == 'POST':
        author_name = request.POST.get('author_name')
        birth_date = request.POST.get('birth_date')
        country = request.POST.get('country')
        m.BooksManager.add_author(m.Authors, author_name=author_name, birth_date=birth_date, country=country)
        return HttpResponse(render(request, template_name='success.html'))

    return HttpResponse(render(request, template_name='add_author.html'))


def add_book(request):
    if request.method == 'POST':
        book_name = request.POST.get('book_name')
        author_id = request.POST.get('author_id')
        m.BooksManager.add_book(m.Books, book_name=book_name, author_id=author_id)
        return HttpResponse(render(request, template_name='success.html'))

    options = m.BooksManager.get_authors(m.Authors)
    context = {'options': options}

    return HttpResponse(render(request, template_name='add_book.html', context=context))


def add(request):
    if request.method == 'POST':

        values = ('author', 'book')
        value = ''.join(tuple(filter(lambda value: value in request.POST.keys(), values)))
        if value in values:
            if value == 'author':
                return redirect(add_author)
            return redirect(add_book)
        
    return HttpResponse(render(request, template_name='add_index.html'))


def view(request):

    if request.method == 'GET':

        return HttpResponse(render(request, template_name='index.html'))

    elif request.method == 'POST':
        if request.POST.get('get'):
            return HttpResponse('На стадии разработки')
        elif request.POST.get('add'):
            return redirect(add)
        else:
            return HttpResponseNotFound('Ошибка')

