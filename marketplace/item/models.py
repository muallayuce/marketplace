from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name= models.CharField(max_length=255)
    
    class Meta:
        ordering = ('name',)
        verbose_name_plural = "Categories"
        
        
    def __str__(self):
        return self.name


class Item(models.Model):
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    name= models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    image= models.ImageField(upload_to='item_images', blank=True, null= True)
    is_sold = models.BooleanField(default=False) #The prefix "is_" is used to imply that the field is a boolean flag or indicator. It makes the code more readable and helps developers and maintainers understand that the field is a boolean variable. This naming convention provides clarity about the purpose of the field, making the code easier to understand and maintain.
    created_by = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name