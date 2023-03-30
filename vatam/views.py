from django.shortcuts import render
from .models import Order       #men qoshdim(0323)
from .forms import OrderForm


# Create your views here.
def first_page(request):
    object_list=Order.objects.all()     #men qoshdim(0323)
    form=OrderForm()
    return render(request, './index.html', {'object_list': object_list,
                                            'form': form}) #men qoshdim(0323)


def thanks_page(request):
    # name = request.GET['name']
    # phone = request.GET['phone']

    name = request.POST['name']
    phone = request.POST['phone']
    element = Order(order_name=name, order_phone=phone)
    element.save()
    return render(request, './thanks_page.html', {'name':name,
                                                  'phone': phone})