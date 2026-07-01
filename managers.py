from django.contrib.auth.base_user import BaseUserManager
class UserManager(BaseUserManager):
#our cutom manager for the user model instead of django's default user creation because of this we will define our own rules for creating users and superusers
    def create_user(self, username, email, password=None, **extra_fields):
#by using this function we can create a user with the given username, email, and password
        if not email:#evry acc must have an email address so if the email is not provided we will raise a value error
            raise ValueError('The Email field must be set')
        if not username:
            raise ValueError('The Username field must be set')
        email = self.normalize_email(email)# it convert email into a standard format by lowercasing the domain part of the email address
        user = self.model(username=username, 
                          email=email, 
                          **extra_fields)# create a user object int he memory but nothing is getting saved rn innto the database 
        user.set_password(password)
        # never save password directly as place text, instead use the has before saving it to the database.
        user.save(using=self._db)# save the user into the database 
        return user
# now rn we are going to create a administrator account this is used while running 
    def create_superuser(self, username, email, password=None, **extra_fields):
        # give admin permissions 
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(
            username, 
            email,
            password, 
            **extra_fields
        )