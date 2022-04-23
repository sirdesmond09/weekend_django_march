from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class BlogPost(models.Model):
    STATUS_CHOICE  = [
        ("draft", "Draft"),
        ("published", "Published")
    ]
    
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    desc = models.CharField(max_length=250)
    body = models.TextField()
    status = models.CharField(max_length=250, choices=STATUS_CHOICE)
    date_created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.title
    