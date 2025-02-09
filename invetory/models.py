from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name=models.CharField(max_length=100)
    class Meta:
        verbose_name_plural='categories'
    def __str__(self):
        return self.name

class Inventory(models.Model):
    name=models.CharField(max_length=100)
    quantity=models.IntegerField()
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    created=models.DateTimeField(auto_now_add=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.name
        
