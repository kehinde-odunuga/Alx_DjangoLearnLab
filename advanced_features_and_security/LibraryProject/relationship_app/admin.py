from django.contrib import admin
from .models import Author, Book, Library, Librarian

# Register your models here.
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)        
    search_fields = ('name',)
    
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')  
    list_filter = ('title', 'author')            
    search_fields = ('title', 'author')         
    
class LibraryAdmin(admin.ModelAdmin):
    # list_display = ('name', 'books')
    list_filter = ('name', 'books')            
    search_fields = ('name', 'books')
    
class LibrarianAdmin(admin.ModelAdmin):
    list_display = ('name', 'library')
    list_filter = ('name', 'library')         
    search_fields = ('name', 'library')           
          
    
# Register your models here.
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Library, LibraryAdmin) 
admin.site.register(Librarian, LibrarianAdmin) 