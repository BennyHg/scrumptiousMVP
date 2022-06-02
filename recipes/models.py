from django.db import models


# Create your models here.
class Recipe(models.Model):
    name = models.CharField(max_length=125)
    author = models.CharField(max_length=100)
    description = models.TextField()
    image = models.URLField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name + " by " + self.author

class Step(models.Model):
    order = models.SmallIntegerField()
    directions = models.TextField()
    author = models.ForeignKey("Recipe", related_name="steps", on_delete=models.CASCADE)