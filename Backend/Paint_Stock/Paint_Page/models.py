from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import gettext_lazy as _

class Paints(models.Model):
    colour = models.CharField(max_length=50)
    stock_level = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.colour
    
class SiteUserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
                raise ValueError(_('A Username is required'))
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def delete_user(self, user):
         user.delete()
         
class SiteUser(AbstractUser):
    username = models.CharField(unique=True,max_length=30)
    is_admin = models.BooleanField(default=False)
    is_editor = models.BooleanField(default=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    objects = SiteUserManager()

    def __str__(self):
        return self.username
    
