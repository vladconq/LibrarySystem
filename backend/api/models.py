from django.db import models


class AuthorModel(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class ShelfModel(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class BookModel(models.Model):
    name = models.CharField(max_length=200)
    author = models.ForeignKey(AuthorModel, on_delete=models.CASCADE)
    shelf = models.ForeignKey(ShelfModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
