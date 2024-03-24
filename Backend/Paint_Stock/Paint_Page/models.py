from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, Group
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model

User = get_user_model()

#Model for the paint cards, PositiveIntegerField as negative quantities are not possible
class Paints(models.Model):
    colour = models.CharField(max_length=50)
    stock_level = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.colour
    
#User manager, allows for creation and deletion of users in the admin menu
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

#Model for users, variables for admin/editor permissions
class SiteUser(AbstractUser):
    username = models.CharField(unique=True,max_length=30)
    is_admin = models.BooleanField(default=False)
    is_editor = models.BooleanField(default=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    objects = SiteUserManager()

    def __str__(self):
        return self.username
    
@receiver(post_save, sender=User) #ensures only signals from User are used for the instance
def assign_permissions(sender, instance, created, **kwargs):
    if created:
        #creates groups for different permission levels
        editors_group, _ = Group.objects.get_or_create(name='Editors')
        admins_group, _ = Group.objects.get_or_create(name='Admins')

        #sets permissions per group
        editors_group.permissions.add('view_paints', 'edit_paints')
        admins_group.permissions.add('view_paints', 'edit_paints', 'edit_users')

        #assigns new users to groups based on their initial roles
        if instance.is_editor:
            instance.groups.add(editors_group)
        if instance.is_admin:
            instance.groups.add(admins_group)