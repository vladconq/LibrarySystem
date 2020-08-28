from django.urls import path
from . import views

urlpatterns = [
    path('authors/', views.get_authors),
    path('shelves/', views.get_shelves),
    path('authors/<str:author_name>/books/', views.get_books_of_author),
    path('shelves/<str:shelf_name>/shelves/', views.get_books_of_shelf),
]
