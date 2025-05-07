from django.urls import path, include

from rest_framework.routers import DefaultRouter

from apps.apartments.api import views


router = DefaultRouter()
router.register(r'apartments', views.ApartmentViewSet, basename='apartments')

urlpatterns = [
    path('', include(router.urls)),
]