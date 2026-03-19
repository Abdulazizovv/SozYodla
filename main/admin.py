from django.contrib import admin
from main.models import Subject, Word


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "is_public", "created_at", "updated_at"]
    list_display_links = ["title"]


@admin.register(Word)
class WordAdmin(admin.ModelAdmin):
    list_display = ["id", "word", "translated", "created_at", "updated_at"]
    list_display_links = ["word"]
    search_fields = ["word", "translated"]
    list_filter = ["author"]
    prepopulated_fields = {"slug": ("word",)}