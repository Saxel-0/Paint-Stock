from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model

User = get_user_model()

# Function to update permissions on an existing profile
def update_permissions(username, is_editor=False, is_admin=False):
    try:
        # Gets user by username
        user = User.objects.get(username=username)
        
        # Clear their existing group memberships
        user.groups.clear()

        editors_group, _ = Group.objects.get_or_create(name='Editors')
        admins_group, _ = Group.objects.get_or_create(name='Admins')
        
        # Assigns user to new group
        if is_editor:
            user.is_editor = True
            user.groups.add(editors_group)
        if is_admin:
            user.is_admin = True
            user.groups.add(admins_group)

        # Saves the updated user permissions
        user.save()

        return user  
    except User.DoesNotExist:
        return None  # User not found
