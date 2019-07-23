from django.db import models
from users.models import UserTable


# Create your models here.
class my_codes(models.Model):
    """
    Kodların tutulduğu table
    """
    type    = models.CharField(max_length=32, verbose_name='Dokuman Turu')
    code    = models.CharField(max_length=16, verbose_name='Kısa Kodu')
    title   = models.CharField(max_length=32, verbose_name='Kod Açıklaması')

    def __str__(self):
        return self.title


class Documents(models.Model):
    """
    Document Master table dökümana ait
    genel bilgilerin bulunduğu table
    """
    type_id = models.ForeignKey(my_codes, null=True, blank=True, on_delete=models.CASCADE, verbose_name='Dosta Türü')
    title           = models.CharField(max_length=36, verbose_name='Döküman Başlık')
    doc             = models.FileField(verbose_name='Dokumanlarım')
    image           = models.ImageField(verbose_name='Resim Dosyalarım',null=True,blank=True)
    active          = models.BooleanField(default=True)
    comment         = models.TextField(default=256)
    create_date     = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name='Dokuman Ekleme Tarihi')
    revision_date   = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name='Revizyon Tarihi')
    fallow          = models.ManyToManyField('self')


    def __str__(self):
        return self.title

class Documents_Hash(models.Model):
    """
    Document hash table yeni bir döküman
    ekleme sırasın eklenen dökümanla var olan
    döküman ınhash bilgisine bakmak için gerekli gördüğüm table
    """
    doc_id      = models.ForeignKey(Documents,on_delete=models.CASCADE, verbose_name='document_id')
    doc_hash    = models.CharField(max_length=64, verbose_name='document_hash')

class Documents_user(models.Model):
    """
    Kullanıcıların eklemiş oldğu ve
    kullanıcılara göre dökümanlara
    ulaşmak için kullanıdığım table
    """
    user_id     = models.ForeignKey(UserTable, on_delete=models.CASCADE)
    doc_id      = models.ForeignKey(Documents, on_delete=models.CASCADE)

# class favori(models.Model):
#     """
#     Favori Kullanıcı ve Dökümanlanların tutulduğu table
#     """
#     type        = models.CharField(max_length=5, null=True, blank=True)
#     user_id     = models.ManyToManyField(UserTable, blank=True, verbose_name='Kullanıcı Favori')
#     doc_id      = models.ManyToManyField(Documents, blank=True, verbose_name='Dökğman Favori')
