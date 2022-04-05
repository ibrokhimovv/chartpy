from django.db import models

class Post(models.Model):
    class Meta:
        verbose_name = "Post"
        verbose_name_plural = 'Posts'


    name = models.CharField(max_length=50)
    daromadi = models.IntegerField()

    def __str__(self):
        return self.name

class Post2(models.Model):
    class Meta:
        verbose_name = 'Post2'
        verbose_name_plural = 'Posts2'
    
    country = models.CharField(max_length=20)
    rating = models.IntegerField(max_length=2)

    def __str__(self):
        return self.country