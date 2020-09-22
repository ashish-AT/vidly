from django.contrib import admin
from .models import Genre, Movie
# Register your models here.


class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class MovieAdmin(admin.ModelAdmin):
    exclude = ('created_at',)
    list_display = ('title', 'number_in_stock',
                    'released_year', 'genre', 'created_at')


admin.site.register(Genre, GenreAdmin)
admin.site.register(Movie, MovieAdmin)
