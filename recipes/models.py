from django.db import models

class Recipe(models.Model):
    title = models.CharField()
    author = models.CharField()
    content = models.TextField()
    ingredient = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    class Meta:
        ordering = ['-date_created']