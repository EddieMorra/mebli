
from django.contrib import admin
from .models import Category, Product, Gallery, Table, Post, Comment, Dollar, Mainpage
# ItemPrice
from mptt.admin import MPTTModelAdmin
from ckeditor.fields import RichTextField
# from reversion.admin import VersionAdmin




# admin.site.register(Post)
# @admin.register(Post)  
# class PostAdmin(admin.ModelAdmin):  
#     list_display = ('title', )



@admin.register(Mainpage)  
class MainpageAdmin(admin.ModelAdmin):  
    list_display = ('title',)


@admin.register(Dollar)  
class Dollar_dAdmin(admin.ModelAdmin):  
    list_display = ('name', 'num' )
    list_editable = ['num' ]



@admin.register(Comment)  
class CommentAdmin(admin.ModelAdmin):  
    list_display = ('name', 'created', 'updated', 'active')  
    list_filter = ('active', 'created', 'updated')  
    search_fields = ('name', 'email', 'body')



class GalleryInline(admin.TabularInline):
    fk_name = 'product'
    model = Gallery

class TableInline(admin.TabularInline):
    fk_name = 'product'
    model = Table




# class CommentAdmin(admin.ModelAdmin):
#     list_display = ['title', 'slug']
    # prepopulated_fields = {'slug': ('name', )}

# Модель категории
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'parent']
    list_editable = ['parent', ]
    prepopulated_fields = {'slug': ('name', )}
# Модель товара
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price',
    # 'kurs',
    'available', 'created', 'updated']
    list_filter = ['name', 'available', 'created', 'updated']
    list_editable = ['available', 'price', 
    # 'kurs'
    ]
    search_fields = ['name', 'description']
    inlines = [GalleryInline, TableInline, ]
    prepopulated_fields = {'slug': ('name', )}

class CustomMPTTModelAdmin(MPTTModelAdmin):
    # specify pixel amount for this ModelAdmin only:
    mptt_level_indent = 20

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)



