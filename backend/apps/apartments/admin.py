from django.contrib import admin

from apps.apartments.models import Apartment


@admin.register(Apartment)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'number_of_rooms', 'square', 'availability', 'created_at', 'updated_at']
    list_filter = ['name', 'price', 'number_of_rooms', 'square', 'availability', 'created_at']
    search_fields = ['name']
    ordering = ['name', 'price', 'number_of_rooms', 'square', 'availability']

    fieldsets = (
        ('Apartment', {'fields': ('name', 'slug', 'description', 'price', 'number_of_rooms', 'square', 'availability', 'owner')}),
    )
    add_fieldsets = (
        ('Apartment', {'fields': ('name', 'slug', 'description', 'price', 'number_of_rooms', 'square', 'availability', 'owner')}),
    )
    filter_horizontal = ()
    ordering = ('name',)
