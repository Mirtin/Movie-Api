from django.db import models
from django.core.files.base import ContentFile
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import os
from PIL import Image
from io import BytesIO


class ProfileModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    avatar = models.ImageField(upload_to="accounts/user/avatar", default=None)

    def save(self, *args, **kwargs):

        if self.pk:
            old_avatar = ProfileModel.objects.get(pk=self.pk).avatar
            if old_avatar and old_avatar != self.avatar:
                if os.path.isfile(old_avatar.path):
                    os.remove(old_avatar.path)

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


@receiver(post_save, sender=User)
def manage_user_profile(sender, instance, created, **kwargs):
    if created:
        ProfileModel.objects.create(user=instance)
    else:
        user_profile, created = ProfileModel.objects.get_or_create(user=instance)
        if not created:
            user_profile.save()