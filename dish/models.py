import time
from uuid import uuid4
from django.db import models
from PIL import Image  # to work with image
# from django.contrib.auth.models import User
from django.conf import settings
import os

# Create your models here.
"""
So what is model?
How Data get stored ?
Is creating class a necessay

To-Do
1. Read documentation and source code of models- but why?
2. 

"""

# def path_and_rename(instance, filename):
#     upload_to = 'photos'
#     ext = filename.split('.')[-1]
#     # get filename
#     if instance.pk:
#         filename = '{}.{}'.format(instance.pk, ext)
#     else:
#         # set filename as random string
#         filename = '{}.{}'.format(uuid4().hex, ext)
#     # return the whole path to the file
#     return os.path.join(upload_to, filename)
# # # f"Hello, {name}. You are {age}."

class Dish(models.Model):
    title = models.TextField()
    description = models.TextField(max_length=800)
    recipeurl= models.URLField(max_length=200, blank=True)
    recipeimage = models.ImageField(upload_to= 'photos/%Y/%m/%d')
    created = models.DateTimeField(auto_now_add=True)
    hunter = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    # we are overriding save method
    # via super() we can inherit all the attributes anf properties of save method already written
    # how to get url for recipeimage
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img= Image.open(self.recipeimage.path) # opening image
        # img.name = f"{self.title}-{self.id}-{self.hunter}"
        if img.height > 300 or img.width > 300 :
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.recipeimage.path)

    def summary(self):
        return self.description[:100]

# Create your models here.
