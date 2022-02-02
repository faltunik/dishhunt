from django.db import models
from PIL import Image  # to work with image
# from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
"""
So what is model?
How Data get stored ?
Is creating class a necessay

To-Do
1. Read documentation and source code of models- but why?
2. 

"""

# def user_directory_path(instance, filename):
#     # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
#     return f"{y/m/d}/{instance.recipe.id}"
# # f"Hello, {name}. You are {age}."

class Dish(models.Model):
    title = models.TextField()
    description = models.TextField(max_length=800)
    recipeurl= models.URLField(max_length=200, blank=True)
    recipeimage = models.ImageField(upload_to= 'recipe/%Y/%m/%d/')
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
        if img.height > 300 or img.width > 300 :
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.recipeimage.path)

    def summary(self):
        return self.description[:100]

# Create your models here.
