from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Post model
class Post(models.Model):
    title = models.CharField(max_length=100)

    # Use text field for multi-line content
    content = models.TextField()

    # Defaults to the time the model instance was created
    date_posted = models.DateTimeField(default=timezone.now)

    # Links a user to the creation of the post in a one to many relationship
    # (Users can create multiple posts, but only one user is associated with each post)
    # on_delete: is a user is deleted, delete all their posts too
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    # Specifies which field should be used when displaying the query contents
    def __str__(self):
        return self.title