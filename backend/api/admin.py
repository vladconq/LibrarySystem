from django.contrib import admin
from .models import AuthorModel, BookModel, ShelfModel

admin.site.register(AuthorModel)
admin.site.register(BookModel)
admin.site.register(ShelfModel)
