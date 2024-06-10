from django.db import models
from django.core.exceptions import ObjectDoesNotExist


class BooksManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset()

    def add_author(self, author_name, birth_date, country):
        try:
            migration = Authors.objects.get(author_name=author_name)
        except ObjectDoesNotExist:
            migration = Authors(author_name=author_name, birth_date=birth_date, country=country)
            migration.save()


class Books(models.Model):
    class Meta:
        db_table = 'Books'
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

    id = models.BigAutoField(primary_key=True, unique=True)
    book_name = models.TextField(max_length=128)
    author_name = models.ForeignKey('Authors', on_delete=models.CASCADE)

    objects = BooksManager()

    def __str__(self):
        return f'{self.id, self.book_name, self.author_name}'


class Authors(models.Model):
    class Meta:
        db_table = 'Authors'
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'

    id = models.BigAutoField(primary_key=True, unique=True)

    author_name = models.TextField(max_length=64)
    birth_date = models.DateField()
    country = models.TextField(max_length=64, default=None)

    objects = BooksManager()

    def __str__(self):
        return f'{self.id, self.author_name, self.birth_date, self.country}'
