from django.db import models


# Create your models here.


class File(models.Model):
    title = models.CharField(max_length=16, verbose_name='Dosya Adı', blank=True, null=True)
    file = models.FileField(upload_to='documents/%Y/%m/%d', verbose_name='Dokumanlarım', blank=True, null=True)

    def __str__(self):
        return self.file.name


# https://www.techiediaries.com/django-rest-image-file-upload-tutorial/
