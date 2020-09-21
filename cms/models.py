from django.db import models


class Book(models.Model):
    """Book"""
    name = models.CharField('Books',max_length=255)
    publisher = models.CharField('Office',max_length=255,blank=True)
    page = models.IntegerField('Pages',blank=True,default=0)

    def __str__(self):
        return self.name

class Impression(models.Model):
    """Impression"""
    book = models.ForeignKey(Book,verbose_name='Books',related_name='impressions',on_delete=models.CASCADE)
    comment = models.TextField('comments',blank=True)

    def __str__(self):
        return self.comment
