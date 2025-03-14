from django.urls import path, include
from django.views.decorators.cache import cache_page

from rest_framework import routers

from bookshop import views

router = routers.SimpleRouter()
router.register(r'books', views.BookViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('authors/', views.AuthorListView.as_view(), name='authors'),
    path('sendmail/', views.SendEmail.as_view(), name='sendmail'),
]
