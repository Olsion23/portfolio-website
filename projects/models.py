from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    descriptions = models.TextField()
    link = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class Skill(models.Model):
    name = models.CharField(max_length=200)
    level = models.PositiveIntegerField(max_length=100, blank=True, null=True, default=0, help_text='Enter level from 0 to 100')

    def __str__(self):
        return self.name
    
class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"
# Create your models here.
