from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название книги')
    author = models.ManyToManyField('Author', related_name='books', verbose_name='Автор(ы)')
    language = models.ManyToManyField('Language', related_name='books')
    release_date = models.DateField(verbose_name='Дата выпуска')

    def __str__(self):
        return f"{self.title}"

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['title', 'release_date'], name='book unique')
        ]
        ordering = ['title']


class Author(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя')
    surname = models.CharField(max_length=255, verbose_name='Фамилия')
    location = models.ForeignKey(
        'Location',
        on_delete=models.SET_NULL,
        null=True,
        related_name='authors',
        verbose_name='Местоположение'
    )

    def __str__(self):
        return f"{self.name} {self.surname}"

    class Meta:
        ordering = ['name', 'surname']


class Location(models.Model):
    country = models.CharField(max_length=255, verbose_name='Страна')
    city = models.CharField(max_length=255, verbose_name='Город')

    def __str__(self):
        return f"{self.country}, {self.city}"

    class Meta:
        indexes = [
            models.Index(fields=['country', 'city']),
        ]
        constraints = [
            models.UniqueConstraint(fields=['country', 'city'], name='location unique')
        ]
        ordering = ['country', 'city']


class Language(models.Model):
    language = models.CharField(max_length=255, verbose_name='Язык')

    class Meta:
        indexes = [
            models.Index(fields=['language']),
        ]
        ordering = ['language']
