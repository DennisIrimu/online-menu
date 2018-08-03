from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200,db_index=True)
    slug = models.SlugField(max_length=200,db_index=True,blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

class Food(models.Model):
    category = models.ForeignKey(Category,related_name='foods')
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True,blank=True)
    image = models.ImageField(upload_to='foods/%Y/%m/%d',blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'))

    def __str__(self):
        return self.name
