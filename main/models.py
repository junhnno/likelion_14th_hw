from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=50)
    writer = models.CharField(max_length=30)
    content = models.TextField()
    pub_date = models.DateTimeField()
    grade = models.CharField(max_length=2, default='F') 

    def summary(self):
        return self.content[:20]
