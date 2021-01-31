from django.shortcuts import render, redirect, reverse
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from movies import models as movie_models
from books import models as book_models
from . import models
from . import forms

# Create your views here.


def create_movie_review(request, pk):
    if request.method == "POST":
        form = forms.CreateReviewForm(request.POST)
        movie = movie_models.Movie.objects.get_or_none(pk=pk)
        if not movie:
            return redirect(reverse("core:home"))
        if form.is_valid():
            review = form.save()
            review.movie = movie
            review.created_by = request.user
            review.save()
            return redirect(reverse("movies:movie", kwargs={"pk": movie.pk}))


def create_book_review(request, pk):
    if request.method == "POST":
        form = forms.CreateReviewForm(request.POST)
        book = book_models.Book.objects.get_or_none(pk=pk)
        if not book:
            return redirect(reverse("core:home"))
        if form.is_valid():
            review = form.save()
            review.book = book
            review.created_by = request.user
            review.save()
            return redirect(reverse("books:book", kwargs={"pk": book.pk}))


@login_required
def delete_book_review(request, book_pk, review_pk):
    user = request.user
    try:
        book = book_models.Book.objects.get(pk=book_pk)
        review = book.reviews.get(pk=review_pk)
        if review.created_by.pk != user.pk:
            return redirect(reverse("core:home"))
        else:
            del_review = models.Review.objects.get(pk=review_pk)
            del_review.delete()
        return redirect(reverse("books:book", kwargs={"pk": book_pk}))
    except book_models.Book.DoesNotExist or models.Review.DoesNotExist:
        return redirect(reverse("core:home"))


@login_required
def delete_movie_review(request, movie_pk, review_pk):
    user = request.user
    try:
        movie = movie_models.Movie.objects.get(pk=book_pk)
        review = movie.reviews.get(pk=review_pk)
        if review.created_by.pk != user.pk:
            return redirect(reverse("core:home"))
        else:
            del_review = models.Review.objects.get(pk=review_pk)
            del_review.delete()
        return redirect(reverse("movies:movie", kwargs={"pk": movie_pk}))
    except movie_models.Movie.DoesNotExist or models.Review.DoesNotExist:
        return redirect(reverse("core:home"))