from django.db import models
from django.utils import timezone
from base.models import BaseModel

# Create your models here.

class Category(BaseModel):
    category_name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, null=True, blank=True)
    category_images = models.ImageField(upload_to='categories')


class Paper_Model(BaseModel):
    paper_name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='papers')
    paper_description = models.TextField()


class Paper_Image(BaseModel):
    paper = models.ForeignKey(Paper_Model, on_delete=models.CASCADE, related_name='paper_images')
    image = models.ImageField(upload_to='paper')