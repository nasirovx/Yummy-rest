from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Starters, Breakfast, Lunch, Dinner, Testimonials, Events, Role, Chefs, \
    Book_A_Table, Gallery, Contact
# Register your models here.


@admin.register(Starters)
class StartersAdmin(admin.ModelAdmin):
    list_display = ["title", "description", "price", "created_at", "get_image"]
    list_editable = ["price"]
    list_filter = ["created_at"]
    search_fields = ["title", "description"]

    def get_image(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="100">')
        return "Not image"


@admin.register(Breakfast)
class BreakfastAdmin(admin.ModelAdmin):
    list_display = ["title", "description", "price", "created_at", "get_image"]
    list_editable = ["price"]
    list_filter = ["created_at"]
    search_fields = ["title", "description"]

    def get_image(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="100">')
        return "Not image"


@admin.register(Lunch)
class LunchAdmin(admin.ModelAdmin):
    list_display = ["title", "description", "price", "created_at", "get_image"]
    list_editable = ["price"]
    list_filter = ["created_at"]
    search_fields = ["title", "description"]

    def get_image(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="100">')
        return "Not image"


@admin.register(Dinner)
class DinnerAdmin(admin.ModelAdmin):
    list_display = ["title", "description", "price", "created_at", "get_image"]
    list_editable = ["price"]
    list_filter = ["created_at"]
    search_fields = ["title", "description"]

    def get_image(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="100">')
        return "Not image"


@admin.register(Testimonials)
class TestimonialsAdmin(admin.ModelAdmin):
    list_display = ["full_name", "description", "profession", "created_at", "get_image"]
    list_filter = ["created_at", "profession"]
    search_fields = ["first_name", "last_name", "description"]

    def get_image(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="100">')
        return "Not image"
    

@admin.register(Events)
class EventsAdmin(admin.ModelAdmin):
    list_display = ["title", "description", "price", "created_at", "get_image"]
    list_filter = ["created_at"]
    search_fields = ["title", "description"]

    def get_image(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="100">')
        return "Not image"
    

@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ["title", "created_at"]
    list_filter = ["created_at"]
    search_fields = ["title"]


@admin.register(Chefs)
class ChefsAdmin(admin.ModelAdmin):
    list_display = ["full_name", "role", "created_at", "get_image"]
    list_filter = ["role", "created_at"]
    list_editable = ["role"]
    search_fields = ["full_name"]

    def get_image(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="100">')
        return "Not image"


@admin.register(Book_A_Table)
class Book_A_TableAdmin(admin.ModelAdmin):
    list_display = ["full_name", "email", "phone", "date", "time", "people", "message", "created_at"]
    list_filter = ["date", "time",  "people", "created_at"]
    search_fields = ["date", "time", "full_name"]


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ["get_image", "created_at"]
    list_filter = ["created_at"]

    def get_image(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="100">')
        return "Not image"


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ["full_name", "email", "subject", "message", "created_at"]
    list_filter = ["created_at"]
    search_fields = ["full_name", "email", "subject"]