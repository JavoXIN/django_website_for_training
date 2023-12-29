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
    order_day = models.DateField(verbose_name='Order day')      #tegdim 05.23, 25
    order_time = models.TimeField(verbose_name='Order time')     #tegdim 05.23, 25

    def __str__(self):
        return self.order_name

    class Meta:
        verbose_name = 'ClientOrder'
        verbose_name_plural = 'Client Orders'

class ComentVatam(models.Model):
    coment_binding = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='Applying')
    coment_text = models.TextField(verbose_name='Texts of comments')
    coment_dt = models.DateTimeField(auto_now=True, verbose_name='Date of made')
    coment_date = models.DateField(verbose_name='Date for order')   #ya dobavil 0524. etogo ne bila
    coment_time = models.TimeField(verbose_name='Time for order')   #ya dobavil 0524. etogo ne bila

    def __str__(self):
        return self.coment_text

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'




# Create your models here.
