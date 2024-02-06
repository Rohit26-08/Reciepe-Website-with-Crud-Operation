from django.db import models

# Create your models here.
class insertvalue(models.Model):
    recipe_name=models.CharField(max_length=100)
    recipe_description=models.CharField(max_length=255)
    image1=models.ImageField(upload_to='image')
    
