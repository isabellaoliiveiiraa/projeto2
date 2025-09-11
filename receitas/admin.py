from django.contrib import admin
from django.utils.html import format_html
from .models import Receita

@admin.register(Receita)
class ReceitaAdmin(admin.ModelAdmin):
    list_display = ('title', 'categoria', 'created_at', 'image_preview')
    list_filter = ('categoria', 'created_at')
    search_fields = ('title', 'description', 'ingredients')
    readonly_fields = ('created_at', 'updated_at', 'image_preview')

    def image_preview(self, obj):
        if obj.image:
            return format_html(f'<img src="{obj.image.url}" style="max-width: 100px; max-height: 100px;" />')
        return "Sem imagem"

    image_preview.short_description = "Pré-visualização"