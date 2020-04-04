from django.db import models
from django.urls import reverse
from datetime import datetime
import mptt
from mptt.models import MPTTModel, TreeForeignKey
from ckeditor.fields import RichTextField
from embed_video.fields import EmbedVideoField

class Dollar(models.Model):
    name = models.CharField(max_length=30)
    num = models.FloatField(verbose_name="Курс валют")
    # parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    class Meta:
        verbose_name = 'Курс доллару'
        verbose_name_plural = 'Курс доллару'

    def __str__(self):
        return self.name

# Модель категории
class Category(MPTTModel):
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    name = models.CharField(max_length=200, db_index=True, verbose_name="Імя категорії")
    slug = models.SlugField(max_length=200, db_index=True, unique=True)
    image = models.ImageField(upload_to='categories/%Y/%m/%d/', blank=True, verbose_name="Зображення категорії")
    slider = models.BooleanField(default=False, verbose_name="Слайдер")
    created = models.DateTimeField(default=datetime.now)
    
    class Meta:
        ordering = ['name']
        verbose_name = 'Категорія'
        verbose_name_plural = 'Категорії'

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:ProductListByCategory', args=[self.slug])

mptt.register(Category, order_insertion_by=['name'])




def get_foo(request):
    posts = Kurs_d.objects.filter(id=7)


def dollar(request):
    dollar = Dollar.objects.filter(id=1)



# Модель продукта
class Product(models.Model):
    category = TreeForeignKey(Category, related_name='products', verbose_name="Категорія", on_delete=models.CASCADE)
    # dollar = TreeForeignKey(Dollar, related_name='dollar', default=dollar, verbose_name="Курс", on_delete=models.CASCADE)

    name = models.CharField(max_length=200, db_index=True, verbose_name="Назва")
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d/', blank=True, verbose_name="Головне зображення товару")
    description = RichTextField(blank=True, verbose_name="Опис", max_length=1000,)
    price = models.DecimalField(decimal_places=0, db_index=False, max_digits=10, verbose_name="Ціна в доларах")
    # stock = models.PositiveIntegerField(verbose_name="На складе")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Опубліковано")
    updated = models.DateTimeField(auto_now=True, verbose_name="Оновлено")
    video = EmbedVideoField(null=True, blank=True, verbose_name='Посилання на відео')
    slider = models.BooleanField(default=False, verbose_name="Слайдер")
    # kurs = models.DecimalField(max_digits=20, decimal_places=2, default=26.34, verbose_name='Курс долару')
    available = models.BooleanField(default=True, verbose_name="Показувати на сайті (Товар)")
    
    # def price_uah(self):
    #     itog = self.kurs * self.price
    #     return itog

    # def price_uah2(self, Dollar):
    #         itog2 = Dollar.num * self.price
    #         return itog2

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товари'
        ordering = ['name']
        index_together = [
            ['id', 'slug']
        ]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:ProductDetail', args=[self.id, self.slug])




    # def get_cat_list(self):
    #     k = self.category # for now ignore this instance method
        
    #     breadcrumb = ["dummy"]
    #     while k is not None:
    #         breadcrumb.append(k.slug)
    #         k = k.parent
    #     for i in range(len(breadcrumb)-1):
    #         breadcrumb[i] = '/'.join(breadcrumb[-1:i-1:-1])
    #     return breadcrumb[-1:0:-1]


# class Kurs(models.Model):
#     znachenn = models.CharField(max_length=200, db_index=True, verbose_name="Значення")
#     product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='table')
#     def __str__(self):
#         return self.znachenn

# class CartItem(models.Model): 
#     cart = models.ForeignKey(Cart) 
#     item = models.ForeignKey(Supplier) 
#     quantity = models.IntegerField(default=0) 
#     @property def total_cost(self): 
#         return self.quantity * self.item.retail_price 
#         def __unicode__(self): 
#             return self.item.product_name         

class Gallery(models.Model):
    image = models.ImageField(upload_to='gallery', verbose_name="Кілька зображень")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    # def __str__(self):
    #     return str(self.image)
class Table(models.Model):
    name = models.CharField(max_length=200, db_index=True, verbose_name="Текст")
    znachenn = models.CharField(max_length=200, db_index=True, verbose_name="Значення")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='table')




class Mainpage(models.Model):
    title = models.CharField(max_length=250) 
    abouttext = RichTextField(blank=True, verbose_name="Про магазин ( Текст )", max_length=10000,)
    contacts = RichTextField(blank=True, verbose_name="Контакти ( Текст )", max_length=1000,)
    footertext = models.CharField(max_length=200, db_index=True, verbose_name="Текст")
    class Meta:
        verbose_name = 'Головна сторінка'
        verbose_name_plural = 'Головна сторінка'

    def __str__(self): 
        return self.title


class Post(models.Model): 
    title = models.CharField(max_length=250) 
    slug = models.SlugField(max_length=250) 
    # body = models.TextField() 
    created = models.DateTimeField(auto_now_add=True) 
    updated = models.DateTimeField(auto_now=True) 
    def __str__(self): 
        return self.title


    def get_absolute_url(self):
        return reverse('shop:post_detail', kwargs={
            'slug': self.slug,
            'id': self.id
            })


class Comment(models.Model):  
    post = models.ForeignKey(Post,  
			     on_delete=models.CASCADE,  
			     related_name='comments')  
    name = models.CharField(max_length=80, verbose_name="Ім'я")  
    # email = models.EmailField(verbose_name="Текст")  
    body = models.TextField(max_length=780, verbose_name="Текст")  
    created = models.DateTimeField(auto_now_add=True)  
    updated = models.DateTimeField(auto_now=True)  
    active = models.BooleanField(default=True)  
      
    class Meta:  
        ordering = ('-created',)  

    class Meta:
        verbose_name = 'Відгук'
        verbose_name_plural = 'Відгуки'
        ordering = ['created']



    def __str__(self):  
        return 'Відгук {} від {}'.format(self.name, self.post)