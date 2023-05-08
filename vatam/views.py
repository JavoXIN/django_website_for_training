from django.shortcuts import render
from .models import Order       # men qoshdim(0323)
from .forms import OrderForm
from cms2.models import Cms2Slider
from price.models import PriceCard, PriceTable
# Create your views here.
def first_page(request):
    slider_list = Cms2Slider.objects.all()
    pc_1 = PriceCard.objects.get(pk=1)
    pc_2 = PriceCard.objects.get(pk=2)
    pc_3 = PriceCard.objects.get(pk=3)
    price_table = PriceTable.objects.all()
    form = OrderForm()
    dict_obj = {'slider_list': slider_list,
                'pc_1': pc_1,
                'pc_2': pc_2,
                'pc_3': pc_3,
                'price_table': price_table,
                'form': form,
                }

    # form = OrderForm() # 0427 Cms2Slider qoshgandan keyin bu kerakmas boldi
    return render(request, './index.html', dict_obj)  # men qoshdim(0323)


def thanks_page(request):
    # name = request.GET['name']
    # phone = request.GET['phone']

    name = request.POST['name']
    phone = request.POST['phone']
    element = Order(order_name=name, order_phone=phone)
    element.save()
    return render(request, './thanks_page.html', {'name': name,})
