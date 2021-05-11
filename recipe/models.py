from django.db import models

class Recipe(models.Model):
    recipe_name = models.CharField(max_length=100)
    ingredients = models.CharField(max_length=200)
    process = models.TextField()
    image = models.ImageField(upload_to='media/')
    pub_date=models.DateTimeField()

    def __str__(self):
        return self.recipe_name