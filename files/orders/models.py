from django.db import models
from shop.models import Product


class Order(models.Model):
    first_name = models.CharField(verbose_name="Ім'я", max_length=50)
    last_name = models.CharField(verbose_name='Призвіще', max_length=50)
    phone = models.CharField(verbose_name='Телефон', max_length=50, default='+380', db_index=True)
    created = models.DateTimeField(verbose_name='Створено', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='Оновлено', auto_now=True)
    # paid = models.BooleanField(verbose_name='Оплачен', default=False)

    class Meta:
        ordering = ('-created', )
        verbose_name = 'Замовлення'
        verbose_name_plural = 'Усі замовлення'

    def __str__(self):
        return 'Замовлення: {}'.format(self.first_name)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())

    # def get_absolute_url(self):
    #     return reverse('order:OrderCreate', args=[self.id, self.slug])

    

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
    price = models.DecimalField(verbose_name='Ціна', max_digits=10, decimal_places=0)
    quantity = models.PositiveIntegerField(verbose_name='Кількість', default=1)
    # kurs = models.DecimalField(max_digits=20, decimal_places=2, verbose_name='Курс долару')

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity