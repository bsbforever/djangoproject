from django.contrib import admin

# Register your models here.
from polls.models import Choice, Poll

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class PollAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    list_display = ('question', 'pub_date')
    search_fields = ['question']
    list_filter = ['pub_date']
    inlines = [ChoiceInline]

admin.site.register(Poll, PollAdmin)
