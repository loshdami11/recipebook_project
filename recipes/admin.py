from django.contrib import admin


from .models import Recipe

class RecipeAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'content', 'date_created']
    search_fields = ['title']
    list_filter = ['author']

admin.site.register(Recipe, RecipeAdmin)
