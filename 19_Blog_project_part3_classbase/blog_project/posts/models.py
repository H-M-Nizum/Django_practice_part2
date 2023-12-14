from django.db import models
from categories.models import Category
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    
    # built many to many relationship (post and category)
    # akta post ar modde multiple category thakte pare abar aki category r multiple post hote parre.
    category = models.ManyToManyField(Category)
    
    # many to one relationship
    # akjon author multiple post likhe ba muultiple post ar akjon author thakte pare
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    # database a name show korar jonne
    def __str__(self):
        return self.title