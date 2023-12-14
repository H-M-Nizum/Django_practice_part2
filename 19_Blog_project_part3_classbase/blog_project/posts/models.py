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
    
    # upload image filed . blank=true and null=true for this field create after some post
    image = models.ImageField(upload_to='posts/media/uploads/', blank=True, null=True)
    
    # database a name show korar jonne
    def __str__(self):
        return self.title
    
# model for comment
class Comment(models.Model):
    # related ar value diye ai field ta access kora jabe
    post = models.ForeignKey(Post, on_delete = models.CASCADE, related_name='comments')
    name = models.CharField(max_length=30)
    # unique = true means ak e email diye multiple comment korte parbe na.
    email = models.EmailField()
    body = models.TextField()
    # auto coment ar date time show korbe
    created_on = models.DateTimeField(auto_now_add = True)
    
    def __str__(self):
        return f"comment by {self.name}"
    