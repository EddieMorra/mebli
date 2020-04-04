from django.views.generic import View
from django.shortcuts import render, get_object_or_404
from .models import Category, Product, Gallery, Mainpage, Table, Post, Comment, Dollar, Mainpage
# , ItemPrice
from cart.forms import CartAddProductForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils import timezone
from datetime import datetime
from django.views.generic import ListView
from django.db.models import Q
#
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic.list import ListView
from django.contrib.admin.models import LogEntry, ADDITION, CHANGE, DELETION

# from .forms import PostForm


from .forms import CommentForm
#, EmailPostForm


# from .views import *

from django.contrib.admin.models import LogEntry, ADDITION, CHANGE, DELETION

# def defcat(request):
#     return Category.objects.get(id=17)

def main(request, template):
    logs = LogEntry.objects.exclude(change_message="No fields changed.").order_by('-action_time')[:20]
    logCount = LogEntry.objects.exclude(change_message="No fields changed.").order_by('-action_time')[:20].count()
    return render(request, template, {"logs":logs, "logCount":logCount})


def base_view(request):
    main = Mainpage.objects.get(id=1)
    # main = Mainpage.objects.all()
    posts = Post.objects.filter(id=1)
    logs = LogEntry.objects.exclude(change_message="No fields changed.").order_by('-action_time')[:20]
    logCount = LogEntry.objects.exclude(change_message="No fields changed.").order_by('-action_time')[:20].count()
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True).order_by('-created')[:9]
    slider_main = Product.objects.filter(slider=True).order_by('-created')
    categories_right_section = Category.objects.filter(slider=True).order_by('-created')[:2]
    # comment = Product.comments.all()
    
    # if category_slug:
    #     category = get_object_or_404(Category, slug=category_slug)
    #     products = products.filter(category=category)
    # dollar = Dollar.objects.all()
    dollar = Dollar.objects.get(id=1)

    context = {
        'category': category,
        'categories': categories,
        'products': products,
        'slider_main': slider_main,
        'categories_right_section': categories_right_section,
        "logs": logs, 
        "logCount": logCount,
        "dollar": dollar,
        # "dollar2": dollar2,
        'posts': posts,
        'main': main,

        # "comment": comment,
      
    }
    return render(request, 'shop/base.html', context)


# Страница с товарами
def ProductList(request, category_slug=None):
    dollar = Dollar.objects.get(id=1)
    posts = Post.objects.filter(id=1)
  

    now = timezone.now()
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True).order_by('-created')
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    page = request.GET.get('page', 1)
    paginator = Paginator(products, 3)
    paginate_by = 5
    model = products
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
        
    
    # branch_categories = Category.objects.get_descendants(include_self=True)
    # category_products = Product.objects.filter(Category__in=branch_categories).distinct()
  
    return render(request, 'shop/product/list.html', {
        'category': category,
        'categories': categories,
        'products': products,
        'posts': posts,
        'dollar': dollar,
        # 'branch_categories': branch_categories,
        # 'category_products': category_products,
    })





# class SearchResultsView(ListView):
#     model = Product
#     template_name = 'shop/product/searchlist.html'

def SearchResultsView(request):
    dollar = Dollar.objects.get(id=1)

    posts = Post.objects.filter(id=1)

    # products = Product.objects.all()
    # products = Product.objects.filter(available=True).order_by('-created')
    search_results = request.GET.get('q', '')

    if search_results:
        products = Product.objects.filter(Q(name__icontains=search_results) | Q(description__icontains=search_results)).order_by('name')
    else:
        products = Product.objects.all()

    page = request.GET.get('page', 1)
    paginator = Paginator(products, 3)
    paginate_by = 5
    # context_object_name = 'products'
    # template_name = 'shop/product/list.html'
    model = products

    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    category = None
    categories = Category.objects.all()

    return render(request, 'shop/product/searchlist.html', {
        'category': category,
        'categories': categories,
        'products': products,
        'posts': posts,
        'dollar': dollar,
        # 'numbers': numbers
    })
    



# Страница товара
def ProductDetail(request, id, slug):
    dollar = Dollar.objects.get(id=1)
    category = None
    categories = Category.objects.all()
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    gallery = Gallery.objects.all()
    table =  Table.objects.all()
    posts = Post.objects.filter(id=1)
    # kurs = Kurs_d.objects.all()
    # ItemPrice = ItemPrice.objects.all()
    return render(request, 'shop/product/detail.html',
                             {  
                                'category': category,
                                'categories': categories,
                                'product': product,
                                'gallery': gallery,
                                'table': table,
                                'posts': posts,
                                'dollar': dollar,
                                # 'kurs': kurs,
                                # 'ItemPrice': ItemPrice,


                                # 'comments': comments,  
                                # 'new_comment': new_comment,  
                                # 'comment_form': comment_form,


                                # 'images': images,
                                'cart_product_form': cart_product_form})



# Страница поста
def post_detail(request, id, slug):
    category = None
    categories = Category.objects.all()
    post = get_object_or_404(Post, id=id, slug=slug)
    # post_1 = Post.objects.get(id=1)

    posts = Post.objects.filter(id=1)
    


    comments = post.comments.filter(active=True)  
    new_comment = None  
    if request.method == 'POST':  
        # Комментарий был опубликован
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Создайте объект Comment, но пока не сохраняйте в базу данных
            new_comment = comment_form.save(commit=False)
                # Назначить текущий пост комментарию
            new_comment.post = post
                # Сохранить комментарий в базе данных 
            new_comment.save()  
    else:  
        comment_form = CommentForm()  
        
 
    return render(request, 'shop/product/comments.html', {  
        'post': post,
        'category': category,
        'categories': categories,
        'posts': posts,


        'post': post,  
        'comments': comments,  
        'new_comment': new_comment,  
        'comment_form': comment_form
        # 'post_1': post_1,
        })




def show_category(request,hierarchy= None):
    category_slug = hierarchy.split('/')
    category_queryset = list(Category.objects.all())
    all_slugs = [ x.slug for x in category_queryset ]
    parent = None
    for slug in category_slug:
        if slug in all_slugs:
            parent = get_object_or_404(Category,slug=slug,parent=parent)
        else:
            instance = get_object_or_404(Product, slug=slug)
            breadcrumbs_link = instance.get_cat_list()
            # print(breadcrumbs_link)
            category_name = [' '.join(i.split('/')[-1].split('-')) for i in breadcrumbs_link]
            breadcrumbs = zip(breadcrumbs_link, category_name)
            return render(request, "detail.html", {
                'instance':instance,
                'breadcrumbs':breadcrumbs
                })

    return render(request,"list.html",{
        'post_set': parent.post_set.all(),
        'sub_categories': parent.children.all()
        })
