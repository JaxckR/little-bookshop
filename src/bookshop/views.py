from rest_framework import generics, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.response import Response

from bookshop.models import Book, Author
from bookshop.serializers import BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    permission_classes = [IsAuthenticated]

    @action(methods=['get'], detail=True)
    def author(self, request, pk=None):
        authors = Author.objects.all()
        if pk is not None:
            authors = authors.get(pk=pk)
            return Response({'author': authors.name})
        return Response({'authors': [str(a) for a in authors]})
