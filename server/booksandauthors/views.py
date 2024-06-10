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
        return HttpResponse(render(request, template_name='add_author_success.html'))

    return HttpResponse(render(request, template_name='add_author.html'))


def add(request):
    if request.method == 'POST':

        #author_name = None
        #birth_date = None
        #city = None
        values = ('author', 'book')
        value = ''.join(tuple(filter(lambda value: value in request.POST.keys(), values)))
        if value in values:
            return redirect(add_author)
        
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
