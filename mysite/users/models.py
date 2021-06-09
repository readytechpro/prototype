from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.core.files.storage import default_storage as storage

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.__resize_image()

    def __resize_image(self):
        MAX_WIDTH = 300
        MAX_HEIGHT = 600
        with Image.open(self.image) as img:
            if img.width > MAX_WIDTH or img.height > MAX_HEIGHT:
                resize_ratio = min(
                    (MAX_WIDTH / img.width), (MAX_HEIGHT / img.height))
                output_size = (int(img.width * resize_ratio), int(img.height * resize_ratio))
                img = img.resize(output_size)

            with storage.open(self.image.name, "w") as file_handler:
                img.save(file_handler, 'png')
            