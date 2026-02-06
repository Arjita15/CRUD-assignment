from django.db import models

class Note(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)   # sets when created
    updated_at = models.DateTimeField(auto_now=True)       # updates on every save

    def __str__(self):
        return self.title
