from django.db import models

# Create your models here.
class place(models.Model):
    name=models.CharField(max_length=100)
    img=models.ImageField(upload_to='product')
    desc=models.TextField()
    price=models.IntegerField()
    offer=models.BooleanField(default=False)

    def __str__(self):
        return self.name

class blog(models.Model):
    date=models.DateField(verbose_name=None,auto_now_add=False)
    title=models.CharField(max_length=100)
    desc=models.TextField()
    img=models.ImageField(upload_to='blogs')

    def __str__(self):
        return self.title