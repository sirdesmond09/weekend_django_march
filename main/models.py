from django.db import models
import uuid
import random

def get_stu_num():
    return int("".join([str(random.choice(range(10))) for _ in range(6)]))


# Create your models here.
class Student(models.Model):
    COURSE_CHOICES = (("backend", "Backend with Django"),
                      ("frontend", "Frontend with React"),
                       ("datascience", "Data science with Python"))
    
    
    id = models.UUIDField(primary_key=True, editable=False, unique=True, default=uuid.uuid4)
    name = models.CharField(max_length=300)
    course = models.CharField(max_length=300, choices=COURSE_CHOICES)
    bio = models.TextField()
    student_num = models.IntegerField(default=get_stu_num, editable=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    
    
    class Meta:
        ordering = ["-date_joined"]
        
    def __str__(self) -> str:
        return self.name
    