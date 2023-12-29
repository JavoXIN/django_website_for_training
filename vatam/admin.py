from django.contrib import admin
from .models import Order, StatusVatam, ComentVatam
# Register your models here.

class Coment(admin.StackedInline):
    model = ComentVatam
    fields = ('coment_dt', 'coment_text')
    readonly_fields = ('coment_dt',)
    extra = 0


class OrderAdm(admin.ModelAdmin):
    #list_display = ('id', 'order_status', 'order_name', 'order_phone', 'order_dt') #original 0523
    list_display = ('id', 'order_status', 'order_name', 'order_phone', 'order_dt', 'order_day', 'order_time',) #ya dobavil 0523 'order_day', 'order_time'
    list_display_links = ('id', 'order_name')
    #search_fields = ('id', 'order_name', 'order_phone', 'order_dt') #original shunaqa edi 0523
    search_fields = ('id', 'order_name', 'order_phone', 'order_dt', 'order_day', 'order_time',) #ya dobavil 0523 'order_day', 'order_time'
    list_filter = ('order_status',)
    list_editable = ('order_status', 'order_phone',)
    list_per_page = 10
    list_max_show_all = 100
    #fields = ('id', 'order_status', 'order_dt', 'order_name', 'order_phone') #original  0523
    fields = ('id', 'order_status', 'order_dt', 'order_name', 'order_phone', 'order_day', 'order_time',) #ya dobavil 0523 'order_day', 'order_time'
    #readonly_fields = ('id', 'order_dt')        #original

    readonly_fields = ('id', 'order_dt', 'order_day', 'order_time',)        #pomenyal 0526

    #for Coment class page
    inlines = [Coment, ]


admin.site.register(Order, OrderAdm)
admin.site.register(StatusVatam)
admin.site.register(ComentVatam)
