from django.contrib import admin
from places.models import Place, Image
from django.utils.html import format_html
from adminsortable2.admin import SortableStackedInline, SortableAdminBase


class ImageInline(SortableStackedInline):
    model = Image
    readonly_fields = ['place_image']
    fields = ['file', 'place_image', 'number']

    def place_image(self, instance):
        return format_html(f'<img src="{instance.file.url}" width="300" height=200 />')


@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]


admin.site.register(Image)
