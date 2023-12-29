from django.shortcuts import render
from .models import Order       # men qoshdim(0323)
from .forms import OrderForm
from cms2.models import Cms2Slider
from price.models import PriceCard, PriceTable
from telebot.sendmessage import sendTelegram
from datetime import datetime

# Create your views here.
def first_page(request):
    slider_list = Cms2Slider.objects.all()
    pc_1 = PriceCard.objects.get(pk=1)
    pc_2 = PriceCard.objects.get(pk=2)
    pc_3 = PriceCard.objects.get(pk=3)
    price_table = PriceTable.objects.all()
    form = OrderForm()

    # men qoshdim 05.23
    all_time = ['09:00', '10:00', '11:00', '12:00',
                '13:00', '14:00', '15:00', '16:00',
                '17:00', '18:00', '19:00', '20:00',
                '21:00', ]

    yesterday = datetime.today()
    min_day_value = yesterday.strftime("%Y-%m-%d")

    # dict_obj = {}   #shuni hal qilish kerak 05.23
    # shotgacha men qoshdim 05.23

    dict_obj = {'slider_list': slider_list,
                'pc_1': pc_1,
                'pc_2': pc_2,
                'pc_3': pc_3,
                'price_table': price_table,
                'form': form,
                'min_day_value': min_day_value,  #mennnnnnn qoshdim 05.23
                'all_time': all_time,  #mennnnnnn qoshdim 05.23
                }


    # form = OrderForm() # 0427 Cms2Slider qoshgandan keyin bu kerakmas boldi
    return render(request, './index.html', dict_obj)  # ya dobavil(0323)


def thanks_page(request):
    if request.POST:
        # name = request.GET['name']
        # phone = request.GET['phone']

        name = request.POST['name']
        phone = request.POST['phone']
        day = request.POST['date']
        time = request.POST['time']

        time = datetime.strptime(time, '%H:%M').time()      #ya dobavil 0526

        element = Order(order_name = name, order_phone = phone, order_day = day, order_time = time)
        element.save()
        sendTelegram(tg_name=name, tg_phone=phone, tg_day=day, tg_time=time)
        return render(request, './thanks.html', {'name': name,})
    else:
        return render(request, './thanks.html')
