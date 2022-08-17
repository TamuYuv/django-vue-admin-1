from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
from dvadmin.utils.models import CoreModel


class CrudDemoModel(CoreModel):
    goods = models.CharField(max_length=255, verbose_name="Product")
    inventory = models.IntegerField(verbose_name="inventory")
    goods_price = models.FloatField(verbose_name="commodity pricing")
    purchase_goods_date = models.DateField(verbose_name="Purchase time")

    class Meta:
        db_table = "goods"
        verbose_name = 'Commodity table'
        verbose_name_plural = verbose_name
        ordering = ('-create_datetime',)