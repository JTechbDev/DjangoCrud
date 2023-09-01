from django.contrib import admin
from .models import Book

# registering the Book to the admin site
admin.site.register(Book)

