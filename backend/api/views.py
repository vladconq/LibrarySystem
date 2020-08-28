from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt

from .models import AuthorModel, BookModel, ShelfModel
from .serializers import AuthorSerializer, BookSerializer, ShelfSerializer


@csrf_exempt
@api_view(['GET'])
def get_authors(request):
    authors = AuthorModel.objects.all()
    serializer = AuthorSerializer(authors, many=True)
    return Response(serializer.data)


@csrf_exempt
@api_view(['GET'])
def get_shelves(request):
    shelves = ShelfModel.objects.all()
    serializer = ShelfSerializer(shelves, many=True)
    return Response(serializer.data)


@csrf_exempt
@api_view(['GET'])
def get_books_of_author(request, author_name):
    books = BookModel.objects.filter(author__name=author_name)
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)


@csrf_exempt
@api_view(['GET'])
def get_books_of_shelf(request, shelf_name):
    books = BookModel.objects.filter(shelf__name=shelf_name)
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)
