from django.contrib import admin
from .models import Topic, Entry

class EntryInline(admin.TabularInline):
    model = Entry
    extra = 0

@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ("text", "owner", "date_added")
    search_fields = ("text", "description", "owner__username")
    inlines = [EntryInline]

@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
    list_display = ("topic", "date_added")
    search_fields = ("text", "topic__text")
