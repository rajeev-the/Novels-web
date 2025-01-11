from django.db import models

# Create your models here.


class Novel(models.Model):
    name = models.CharField(max_length=100)
    

    


class Chapter(models.Model):
    novel = models.ForeignKey(Novel, related_name='chapters', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()

    
