from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import *


class PostAdmin(admin.ModelAdmin):
    save_on_top = True
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('id', 'title', 'slug', 'created_at', 'get_photo')
    list_display_links = ('title',)
    search_fields = ('title',)
    list_filter = ('category',)
    readonly_fields = ('views', 'created_at', 'get_photo')
    fields = (('title', 'slug'), 'content', ('photo', 'get_photo'), 'category', 'tags', 'views', 'created_at')
    filter_horizontal = ('tags',)

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="50">')
        return '-'

    get_photo.short_description = 'Фото'


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Post, PostAdmin)
