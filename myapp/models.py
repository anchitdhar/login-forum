from django.db import models

# Create your models here.
class UserReg(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(null= False)
    phoneno = models.IntegerField()

    def __str__(self):
        name = self.name