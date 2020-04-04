from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import get_object_or_404

from django.shortcuts import render
from .models import OrderItem
from shop.models import Category, Product, Dollar
from .forms import OrderCreateForm
from cart.cart import Cart
from .models import Order
# from .forms import EmailPostForm  

# from .tasks import order_created
from django.core.mail import send_mail

def OrderCreate(request, ):
    # order = get_object_or_404(Order,) 
    dollar = Dollar.objects.get(id=1)

    cart = Cart(request)
    sent = False
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order, 
                                            product=item['product'],
                                            price=item['price'],
                                            quantity=item['quantity'])
                    
            cd = form.cleaned_data   
            # # order_url = request.build_absolute_uri(order.get_absolute_url())   
            subject = '{} ({}) Замовив товар на сайті Meblilubarta " {}"'.format(cd['first_name'], cd['phone'], order.first_name)   
            message = '"{}" Замовив товар, перейдіть на сайт, щоб подивитись замовлення '.format(order.first_name)   
            send_mail(subject, message, 'rom4egful@gmail.com', ['rom4egful@gmail.com'], fail_silently=False)
            sent = True

                
            # order_created.delay(order.id)
            category = None
            categories = Category.objects.all()

            
            # send_mail(subject, message, 'rom4egful@gmail.com', [cd['rom4egful@gmail.com']])   

            return render(request, 'orders/order/created.html', {'order': order,
                                                                'form': form,
                                                                'category': category,
                                                                'categories': categories,
                                                                'dollar': dollar,
            })

    dollar = Dollar.objects.get(id=1)
    form = OrderCreateForm()
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True).order_by('-created')[:1]

    return render(request, 'orders/order/create.html', {'cart': cart,
                                                        'form': form,
                                                        'category': category,
                                                        'categories': categories,
                                                        'products': products,
                                                        'dollar': dollar,
                                                        # 'order': order,
                                                        })


@staff_member_required
def admin_order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)

    return render(request,
                  'admin/orders/order/detail.html',
                  {'order': order,
                  })






