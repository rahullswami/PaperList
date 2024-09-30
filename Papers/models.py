from django.db import models
from django.utils import timezone

# Create your models here.

class Paper_Models(models.Model):
    paper_images = models.ImageField()
    user_name = models.CharField(max_length=100,default='')
    paper_names = models.CharField(max_length=100)
    paper_title = models.CharField(max_length=200, default='')
    paper_categorys = models.CharField(max_length=50,default='')
    paper_disc = models.TextField(max_length=500)
    paper_time = models.TimeField(default=timezone.now)
    paper_date = models.DateField(default=timezone.now)

    def __str__(self) -> str :
        return f"{self.paper_names} -----> ({self.paper_categorys})"

class Note_Models(models.Model):
    note_images = models.ImageField()
    user_name = models.CharField(max_length=100)
    note_names = models.CharField(max_length=100)
    note_title = models.CharField(max_length=200)
    note_categorys = models.CharField(max_length=50)
    note_desc = models.TextField(max_length=500)
    note_time = models.TimeField(default=timezone.now)
    note_date = models.DateField(default=timezone.now)

    def __str__(self) -> str :
        return f"{self.note_names} -----> ({self.note_categorys})"