from django.urls import path
from .views import BooksView, AddBookView, BookDetailView, UpdateBookDetail, SearchView, AddAuthorView, AuthorDetailView, AllBooksView, AllAuthorsView, GenreDetailView
from .views import AuthorsByCharView, BooksByCharView ,DeleteBookDetailView, AuthorAutocompleteView, DownloadEpubView, AddPublisherView, PublisherAutocompleteView, PublisherDetailView

urlpatterns = [
    path("", BooksView.as_view(), name="home"),
    path("pridat-knihu/", AddBookView.as_view(), name="pridat-knihu"),
    path("detail-knihy/<slug:slug>", BookDetailView.as_view(), name="detail-knihy"),
    path("upravit-knihu/<slug:slug>", UpdateBookDetail.as_view(), name="upravit-knihu"),
    path("smazat-knihu/<slug:slug>", DeleteBookDetailView.as_view(), name="smazat-knihu"),
    path("vysledky-hledani", SearchView.as_view(), name="vysledky-hledani"),
    path("pridat-autora", AddAuthorView.as_view(), name="pridat-autora"),
    path("pridat-nakladatelstvi", AddPublisherView.as_view(), name="pridat-nakladatelstvi"),
    path("detail-autora/<slug:slug>", AuthorDetailView.as_view(), name="detail-autora"),
    path("detail-nakladatelstvi/<slug:slug>", PublisherDetailView.as_view(), name="detail-nakladatelstvi"),
    path("vsechny-knihy/", AllBooksView.as_view(), name="vsechny-knihy"),
    path("vsichni-autori/", AllAuthorsView.as_view(), name="vsichni-autori"),
    path("autori-abecedne-<str:char>", AuthorsByCharView.as_view(), name="vsichni-autori-abecedne"),
    path("knihy-abecedne-<str:char>", BooksByCharView.as_view(), name="vsechny-knihy-abecedne"),
    path("zanr-<slug:slug>", GenreDetailView.as_view(), name="zanr"),
    path("author-autocomplete/", AuthorAutocompleteView.as_view(), name="author-autocomplete"),
    path("publisher-autocomplete/", PublisherAutocompleteView.as_view(), name="publisher-autocomplete"),
    path("stahnout-knihu/<slug:slug>", DownloadEpubView.as_view(), name="stahnout-knihu"),
    ]

