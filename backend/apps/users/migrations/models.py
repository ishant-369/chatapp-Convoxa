from django.contrib.auth.models import AbstractUser
from django.db import models
from .managers import UserManager
#import our cutom manager for the user model instead of django's default user 
#now going to the authentication table 
class User(AbstractUser):
    email = models.Email.Field(unique=True)
    # no two acc will not be able to share the same email address.
    bio = models.TextField(blank=True, 
                           null=True)
    #this field is optional and can be left black or null if the user does not want to fill it out.
    objects = UserManager()
    def __str__(self):
        return self.username
    #now i am going to seprate the profile information from the user model and create a new model called profile which will have a one to one relationship with the user model.
    class Profile(models.Model):
        user = models.OneToOneField(
            User,
            on_delete=models.CASCADE
        )
        profile_picture = models.ImageField(
            upload_to='profile_pictures/',
            blank=True,
            null=True
        )
        created_at = models.DateTimeField(
            auto_now_add=True
        )
        def __str__(self):
            return self.user.username
