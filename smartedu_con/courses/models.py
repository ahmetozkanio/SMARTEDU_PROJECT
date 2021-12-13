from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User

from teachers.models import Teacher    

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50, null=True)
    slug = models.SlugField(max_length=50, unique =True)
   
    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=50, null=True)
    slug = models.SlugField(max_length=50, unique =True)
   
    def __str__(self):
        return self.name



class Course(models.Model):
    teacher = models.ForeignKey(Teacher ,null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, unique=True, verbose_name="Kurs Adi",help_text="Kurs adini yaziniz")
    category = models.ForeignKey(Category, null = True, on_delete=models.DO_NOTHING)
    tags = models.ManyToManyField(Tag,blank=True,null=True )
    students = models.ManyToManyField(User, blank=True,related_name='courses_joined')
    description = models.TextField(blank=True,null=True)
    image  = models.ImageField(upload_to="courses/%Y/%m/%d/",default = "courses/default_course_image.png")
    date = models.DateTimeField(auto_now=True)
    avaliable = models.BooleanField(default =True)

    def __str__(self):
        return self.name