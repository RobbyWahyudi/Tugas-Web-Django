from django.db import models

# Create your models here.


class Produk(models.Model):
    nama = models.CharField(max_length=255)
    harga = models.IntegerField()
