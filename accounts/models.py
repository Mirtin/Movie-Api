from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile

class ProfileModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    avatar = models.ImageField(upload_to="accounts/user/avatar")

    def save(self, *args, **kwargs):
        if self.avatar:
            img = Image.open(self.avatar)

            if img.height != 400 or img.width != 400:
                img = img.resize((400, 400), Image.LANCZOS)

                img_io = BytesIO()
                img.save(img_io, format='PNG')
                img_content = ContentFile(img_io.getvalue(), self.avatar.name)
                
                self.avatar.save(self.avatar.name, img_content, save=False)
        
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.username}'s Profile"


