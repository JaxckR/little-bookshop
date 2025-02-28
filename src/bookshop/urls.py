from django.urls import path, include
from rest_framework import routers

from bookshop import views

router = routers.SimpleRouter()
router.register(r'books', views.BookViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
