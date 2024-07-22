from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to="accounts/user/avatar")

    def save(self, *args, **kwargs):
        # Open the uploaded image
        if self.avatar:
            img = Image.open(self.avatar)
            # Resize the image
            if img.height != 400 or img.width != 400:
                img = img.resize((400, 400), Image.LANCZOS)

                # Save the resized image to a BytesIO object
                img_io = BytesIO()
                img.save(img_io, format='PNG')
                img_content = ContentFile(img_io.getvalue(), self.avatar.name)
                
                # Set the image field to the resized image
                self.avatar.save(self.avatar.name, img_content, save=False)
        
        # Call the original save method
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.username}'s Profile"


