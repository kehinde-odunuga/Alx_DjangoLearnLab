from django.contrib import admin
from .models import Book, User, CustomUser
from django.contrib.auth.admin import UserAdmin


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  
    list_filter = ('author', 'publication_year')            
    search_fields = ('title', 'author')                    

class CustomUserAdmin(UserAdmin):
    list_display = ('date_of_birth', 'profile_photo')  
    list_filter = ('date_of_birth')            
    search_fields = ('date_of_birth') 
    
# Register your models here.
admin.site.register(Book, BookAdmin)
admin.site.register(CustomUser, CustomUserAdmin)