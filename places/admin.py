from adminsortable2.admin import SortableStackedInline, SortableAdminBase
from django import forms
from django.contrib import admin
from django.utils.html import format_html
from places.models import Place, Image


class ImageInline(SortableStackedInline):
    model = Image
    readonly_fields = ['place_image']
    fields = ['file', 'place_image', 'number']

    def place_image(self, instance):
        return format_html("<img src='{}' style='max-width:300px; max-height:200px' />",
                           instance.file.url)


@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin, forms.ModelForm):
    inlines = [
        ImageInline,
    ]


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    raw_id_fields = ['place']
    search_fields = ['place__title']
    list_display = ['place', 'number', 'place_image']
    list_filter = ['place']

    def place_image(self, instance):
        return format_html("<img src='{}' style='max-width:300px; max-height:200px' />",
                           instance.file.url)
