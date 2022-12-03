import json

from ast import literal_eval
from django.core import exceptions as djex
from django.http import (
    HttpRequest, HttpResponse, HttpResponseNotFound, HttpResponseBadRequest,
)
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import View

from . import forms, models


def TrailView(request: HttpRequest) -> HttpResponse:
    """
    View for redirecting visitors to login page
    """
    return redirect(reverse('author-login'))


def AuthorLoginView(request: HttpRequest) -> HttpResponse:
    """
    View for rendering author login page
    """
    return render(request, 'vschcp/authorLogin.html')


class Author(View):
    """
    View to manage authors:
    ** get -- retrieve the author;
    ** post -- create new author;
    ** put -- edit the author;
    ** delete -- remove the author;
    """
    def get(self, request: HttpRequest, alias: str) -> HttpResponse:
        # retrieve author
        try:
            __author = models.Author.objects.get(alias=alias).__dict__

        # handle exceptions
        except djex.ObjectDoesNotExist:
            return HttpResponseNotFound('Author not found')

        # if things are fine
        else:
            # prepare author data to render
            __author.pop('_state')
            
            respdct = json.dumps(__author)
            return HttpResponse(
                respdct,
                content_type='application/json',
                status=200
            )
            

    def post(self, request: HttpRequest, alias: str) -> HttpResponse:
        # clean and validate form data
        __form = forms.AuthorForm(request.POST)
        if __form.is_valid():

            # create author
            __form.save()

            # return author data
            respdct = json.dumps(__form.cleaned_data)
            return HttpResponse(
                respdct,
                content_type='application/json',
                status=201
            )

        # if data not valid
        else:
            respdct = json.dumps(__form.errors)
            return HttpResponseBadRequest(respdct)

    def put(self, request: HttpRequest, alias: str) -> HttpResponse:
        # decode request body
        __body: dict = literal_eval(request.body.decode('utf-8', 'ignore'))

        # retrieve author to be updated
        try:
            author: models.Author = models.Author.objects.get(alias=alias)
            # clean and validate form data
            __form = forms.AuthorForm(data=__body, instance=author)
            if __form.is_valid():

                # update author
                __form.save()

                # return author data
                respdct = json.dumps(__form.cleaned_data)
                return HttpResponse(
                    respdct,
                    content_type='application/json',
                    status=204
                )

            # if data not valid
            else:
                respdct = json.dumps(__form.errors)
                return HttpResponseBadRequest(respdct)

        # handle exceptions
        except djex.ObjectDoesNotExist:
            return HttpResponseNotFound('Author not found')

    def delete(self, request: HttpRequest, alias: str) -> HttpResponse:
        return


class Article(View):
    """
    View to manage articles:
    ** get -- retrieve the article;
    ** post -- create new article;
    ** put -- edit the article;
    ** delete -- remove the article;
    """
    def get(self, request: HttpRequest, author: str, title: str) -> HttpResponse:
        # retrieve article
        try:
            __article = models.Article.objects.get(
                author=author,
                title=title
            ).__dict__

        # handle exceptions
        except djex.ObjectDoesNotExist:
            return HttpResponseNotFound('Article not found')

        # if things are fine
        else:
            # prepare author data to render
            __article.pop('_state')

            # response
            respdct = json.dumps(__article)
            return HttpResponse(
                respdct,
                content_type='application/json',
                status=200
            )

    def post(self, request: HttpRequest, author: str, title: str) -> HttpResponse:
        return

    def put(self, request: HttpRequest, author: str, title: str) -> HttpResponse:
        return

    def delete(self, request: HttpRequest, author: str, title: str) -> HttpResponse:
        return


class Feed(View):
    """
    View to manage feed:
    ** get -- retrieve articles
    """
    def get(self, request: HttpRequest) -> HttpResponse:
        return
