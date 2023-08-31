from django.contrib import admin
from .models import Category, IlastoPost,Uniformcolor

class CategoryAdmin(admin.ModelAdmin):

  list_display = ('id', 'title')
  list_display_links = ('id', 'title')

class IlastoPostAdmin(admin.ModelAdmin):
  list_display = ('id', 'title')
  list_display_links = ('id', 'title')

class UniformcolorAdmin(admin.ModelAdmin):
  list_display = ('id', 'title')
  list_display_links = ('id', 'title')


admin.site.register(Category, CategoryAdmin)
admin.site.register(IlastoPost, IlastoPostAdmin)
admin.site.register(Uniformcolor, UniformcolorAdmin)