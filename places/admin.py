from adminsortable2.admin import SortableStackedInline, SortableAdminBase
from django import forms
from django.contrib import admin
from django.db import models
from django.utils.html import format_html
from tinymce.widgets import TinyMCE
from tinymce import models as tinymce_models

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

    formfield_overrides = {
        tinymce_models.HTMLField: {'widget': TinyMCE()}
    }


admin.site.register(Image)
