from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    username = models.CharField(default='user',null=True,max_length=20,unique=True)
    USERNAME_FIELD = "username"

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_groups'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions'
    )


######################################################################################################
#### simple jwt

# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, Group, Permission
# from django.db import models
# import jwt 
# from tascrum.models import Member


# class UserManager(BaseUserManager):
#     def create_user(self, email, password=None, **extra_fields):
#         if not email:
#             raise ValueError('The Email field must be set')
#         email = self.normalize_email(email)
#         user = self.model(email=email, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         user = CustomUser.objects.get(email=email)
#         Member.objects.create(user=user)
#         return user

#     def create_superuser(self, email, password=None, **extra_fields):
#         extra_fields.setdefault('permission_level', 'admin')
#         return self.create_user(email, password, **extra_fields)

# class CustomUser(AbstractBaseUser, PermissionsMixin):
#     first_name = models.CharField(max_length=20)
#     last_name = models.CharField(max_length=20)
#     email = models.EmailField(unique=True)
#     username = models.CharField(default='user',null=True,max_length=20,unique=True)
    
#     #################################################
#     groups = models.ManyToManyField(Group, related_name='custom_users')
#     user_permissions = models.ManyToManyField(Permission, related_name='custom_users')
#     #################################################


#     PERMISSION_CHOICES = (
#         ('user', 'User'),
#         ('moderator', 'Moderator'),
#         ('admin', 'Admin')
#     )
#     permission_level = models.CharField(max_length=20, choices=PERMISSION_CHOICES, default='user')

#     objects = UserManager()

#     USERNAME_FIELD = 'username'
#     # REQUIRED_FIELDS = ['username']

#     class Meta:
#         verbose_name = 'Custom User'
#         verbose_name_plural = 'Custom Users'

#     def __str__(self):
#         return self.email
    
# class LogicUser:
#     def get_user(request):
#         user = None
#         try:
#             email = request.user.email
#             user = CustomUser.objects.get(email=email)
#         except:
#             pass
#         return user
