from rest_framework import serializers

from bookshop.models import Book, Author, Location


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['country', 'city']
        read_only_fields = ['__all__']


class AuthorSerializer(serializers.ModelSerializer):
    location = LocationSerializer()

    class Meta:
        model = Author
        fields = ['id', 'name', 'surname', 'location']
        field_order = ['id', 'name', 'surname', 'location']


class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(many=True)
    release_date = serializers.DateField(format='%d.%m.%Y')
    language = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = ['id', 'language', 'title', 'release_date', 'author']
        field_order = ['id', 'language', 'title', 'release_date', 'author']

    def get_language(self, obj):
        result = ''.join(i.language for i in obj.language.all())
        return result