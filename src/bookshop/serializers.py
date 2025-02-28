from rest_framework import serializers

from bookshop.models import Book, Author


class BookSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(queryset=Author.objects.all(), many=True, slug_field='id')
    release_date = serializers.DateField(format='%d.%m.%Y')

    class Meta:
        model = Book
        fields = ['title', 'release_date', 'author']
        field_order = ['title', 'release_date', 'author']