from django.db import models


class Author(models.Model):
    AuthorId = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32, unique=True)
    url = models.CharField(default=2, editable=True)

    # class Meta:
    #     indexes = [
    #         Index(fields=('name',))
    #     ]
    #
    #     verbose_name = _('Country')
    #     verbose_name_plural = _('Countrys')

    def __str__(self):
        return self.name


class Book(models.Model):
    BookId = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=32, unique=True)
    url = models.CharField(max_length=254)
    AuthorId = models.ForeignKey('news.Author', on_delete=models.CASCADE)

    # class Meta:
    #     indexes = [
    #         Index(fields=('name',))
    #     ]
    #
    #     verbose_name = _('Dealer')
    #     verbose_name_plural = _('Dealers')
