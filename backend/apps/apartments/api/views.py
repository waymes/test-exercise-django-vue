from django.db.models import Q
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from drf_spectacular.utils import (
    extend_schema,
    OpenApiParameter,
)

from apps.apartments.api import serializers
from apps.apartments.models import Apartment

class ApartmentViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ApartmentSerializer
    queryset = Apartment.objects.all().order_by('-created_at')
    filterset_fields = ['name', 'slug']

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [IsAuthenticated()]
        return [AllowAny()]
    
    def get_queryset(self):
        queryset = super().get_queryset()
        params = self.request.query_params

        price_min = params.get('price_min')
        price_max = params.get('price_max')
        rooms = params.get('rooms')
        available = params.get('available')
        search = params.get('search')

        if price_min is not None:
            queryset = queryset.filter(price__gte=price_min)
        if price_max is not None:
            queryset = queryset.filter(price__lte=price_max)
        if rooms is not None:
            queryset = queryset.filter(number_of_rooms=rooms)
        if available is not None:
            if available.lower() == 'true':
                queryset = queryset.filter(availability=True)
            elif available.lower() == 'false':
                queryset = queryset.filter(availability=False)
        if search:
            queryset = queryset.filter(
                Q(name__icontains=search) | Q(description__icontains=search)
            )

        return queryset

    @extend_schema(
        description='Apartments list (for any user)',
        parameters=[
            OpenApiParameter(
                name='price_min',
                description='Filter by min price',
                required=False,
            ),
            OpenApiParameter(
                name='price_max',
                description='Filter by max price',
                required=False,
            ),
            OpenApiParameter(
                name='rooms',
                description='Filter by rooms number',
                required=False,
            ),
            OpenApiParameter(
                name='available',
                description='Filter by availability',
                required=False,
                type=bool
            ),
            OpenApiParameter(
                name='search',
                description='Search in name or description',
                required=False,
            )
        ],
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    @extend_schema(
        description='Apartment details (for any user)',
        responses={200: serializers.ApartmentSerializer}
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    @extend_schema(
        description='Apartment create (for registered user)',
        responses={200: serializers.ApartmentSerializer}
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    @extend_schema(
        description='Apartment update (for registered user)',
        responses={200: serializers.ApartmentSerializer}
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    

    @extend_schema(
        description='Apartment partial update (for registered user)',
        responses={200: serializers.ApartmentSerializer}
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)
    
    @extend_schema(
        description='Apartment delete (for registered user)',
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
