from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

class Snack(models.Model):
    name = models.CharField(max_length=100)
    purchaser = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    description = models.TextField(default='write about it')
    

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('detail_view', args=[str(self.id)])