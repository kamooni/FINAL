from django.urls import path
from . import views

app_name = "reviews"

urlpatterns = [
    path(
        "movie-review/create/<int:pk>", views.create_movie_review, name="movie-create"
    ),
    path("book-review/create/<int:pk>", views.create_book_review, name="book-create"),
    path(
        "book/<int:book_pk>/review/<int:review_pk>/delete/",
        views.delete_book_review,
        name="delete-book-review",
    ),
    path(
        "movie/<int:movie_pk>/review/<int:review_pk>/delete/",
        views.delete_movie_review,
        name="delete-movie-review",
    ),
]
