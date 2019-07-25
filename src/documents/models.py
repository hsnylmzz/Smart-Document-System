from django.db import models
from accounts.models import CustomUser
from SDS.myFuncitons import Kodlar


class MyCodes(models.Model):
    """
    Kodların tutulduğu table
    """
    type = models.CharField(max_length=32, verbose_name='Dokuman Turu')
    code = models.CharField(max_length=16, verbose_name='Kısa Kodu')
    title = models.CharField(max_length=32, verbose_name='Kod Açıklaması')

    def __str__(self):
        return self.title


"""
type_id de choices a dinamik liste göndermek için
yapılan küçük bir döngü
"""


# x = my_codes.objects.all().filter(type='DOKUMAN')
# xlist = []
# for i in x.values_list('id', 'title'):
#     xlist.append(i)

class Documents(models.Model):
    """
    Document Master table dökümana ait
    genel bilgilerin bulunduğu table

    """
    choices = Kodlar(MyCodes, 'DOKUMANTYPE')
    #
    # choices = [(1,'x')]

    type = models.IntegerField(null=True, blank=True, verbose_name='Dosta Türü', choices=choices)
    label = models.CharField(max_length=36, verbose_name='Döküman Başlık')
    file = models.ImageField(upload_to='documents/%Y/%m/%d', verbose_name='Dokumanlarım', null=True, blank=True)
    image = models.ImageField(verbose_name='Resim Dosyalarım', null=True, blank=True)
    active = models.BooleanField(default=True)
    comment = models.TextField(default=256)
    create_date = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name='Dokuman Ekleme Tarihi')
    revision_date = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name='Revizyon Tarihi')
    file_sha1 = models.CharField(max_length=64, null=True, blank=True, verbose_name='document_hash')
    follow = models.ManyToManyField('self', blank=True)

    def __str__(self):
        return self.label


class DocumentsOwner(models.Model):
    """
    Kullanıcıların eklemiş oldğu ve
    kullanıcılara göre dökümanlara
    ulaşmak için kullanıdığım table
    """
    user_id = models.ForeignKey(CustomUser, to_field='id', on_delete=models.CASCADE)
    doc_id = models.ForeignKey(Documents, to_field='id', on_delete=models.CASCADE)

