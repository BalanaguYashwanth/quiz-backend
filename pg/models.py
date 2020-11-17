from django.db import models
from django.contrib.auth.models import User,auth
from io import BytesIO
from PIL import Image
from django.core.files import File

# Create your models here.

def user_directory_path(instance,filename):
    return 'posts/{0}/{1}'.format(instance.id,filename)

def compress(image):
        im = Image.open(image)
        # create a BytesIO object
        im_io = BytesIO() 
        # save image to BytesIO object
        im.save(im_io, 'JPEG', quality=70) 
        # create a django-friendly Files object
        new_image = File(im_io, name=image.name)
        return new_image

class pgowner(models.Model):
    text=models.TextField()
    img=models.ImageField(upload_to=user_directory_path)

    def save(self, *args, **kwargs):
            if self.img:
                if self.img.size > (300 * 1024):
                    # call the compress function
                    new_image = compress(self.img)
                    # set self.img to new_image
                    self.img = new_image
                    # save
            super().save(*args, **kwargs)



