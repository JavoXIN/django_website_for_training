from django.db import models

class StatusVatam(models.Model):
    Status_name = models.CharField(max_length=200, verbose_name='Status Name')

    def __str__(self):
        return self.Status_name

    class Meta:
        verbose_name = 'Status'
        verbose_name_plural = 'Statuses'




class Order(models.Model):
    order_dt = models.DateTimeField(auto_now=True)
    order_name = models.CharField(max_length=200, verbose_name='Name')
    order_phone = models.CharField(max_length=200, verbose_name='Phone number')
    order_status = models.ForeignKey(StatusVatam, on_delete=models.PROTECT, null=True, verbose_name='Status')

    def __str__(self):
        return self.order_name

    class Meta:
        verbose_name = 'ClientOrder'
        verbose_name_plural = 'Client Orders'

class ComentVatam(models.Model):
    coment_binding = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='Applying')
    coment_text = models.TextField(verbose_name='Texts of commments')
    coment_dt = models.DateTimeField(auto_now=True, verbose_name='Date of made')

    def __str__(self):
        return self.coment_text

    class Meta:
        verbose_name = 'Commentt'
        verbose_name_plural = 'Commentts'




# Create your models here.
