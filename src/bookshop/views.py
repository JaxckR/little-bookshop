from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework import generics, viewsets, status
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from bookshop.models import Book, Author
from bookshop.serializers import BookSerializer, AuthorSerializer
from bookshop.tasks import send_user_email


class BookPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 1000


class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = BookPagination

    @action(methods=['get'], detail=True)
    def author(self, request, pk=None):
        authors = Author.objects.all()
        if pk is not None:
            authors = authors.get(pk=pk)
            return Response({'author': authors.name})
        return Response({'authors': [str(a) for a in authors]})

    @method_decorator(cache_page(60 * 60, key_prefix='drf_page'))
    def list(self, request):
        return super().list(request)


class AuthorListView(generics.ListAPIView):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()


class SendEmail(APIView):

    def post(self, request):
        if not 'email' in request.data:
            return Response({'error': 'Email field is required'}, status=status.HTTP_400_BAD_REQUEST)
        send_user_email.delay(request.data.get('email'))
        return Response({'message': 'mail successful delivered'})