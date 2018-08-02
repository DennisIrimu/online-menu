from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200,db_index=True)

    def __str__(self):
        return self.name

class Food(models.Model):
    category = models.ForeignKey(Category,related_name='foods')
    name = models.CharField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='foods/%Y/%m/%d',blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'price'))

    def __str__(self):
        return self.name
