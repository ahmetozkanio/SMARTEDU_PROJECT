from django.contrib import admin
from . models import Category, Course, Tag

# Register your models here.

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name','avaliable')
    list_filter = ('avaliable',)
    search_fields = ('name',"description")



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    #slug alanimiz otomatik olarak name olarak olusacak ve url icin prepopulated_fields ozelligi
    prepopulated_fields={'slug':('name',)}


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    #slug alanimiz otomatik olarak name olarak olusacak ve url icin prepopulated_fields ozelligi
    prepopulated_fields={'slug':('name',)}