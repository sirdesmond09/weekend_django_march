from django.contrib.auth.models import AbstractUser



class CustomUser(AbstractUser):
    
    
    EMAIL_FIELD = "email"
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email", "first_name", "last_name"]

