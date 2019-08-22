from django.contrib import admin
from book.models import Book

# Register your models here.
class BookAdmin(admin.ModelAdmin):
	class Meta:
		models = Book

admin.site.register(Book, BookAdmin)