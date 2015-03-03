from django.contrib import admin
from books.models import *
# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'publisher', 'publication_date')
    list_filter = ('publisher', 'publication_date')
    ordering = ('-publication_date',)
    search_fields = ('title',)
    fields = ('title','publisher','publication_date','authors',)
    filter_horizontal = ('authors',)

admin.site.register(Book,BookAdmin)
admin.site.register(Publisher)
admin.site.register(Author)
