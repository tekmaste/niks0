from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Category, Order



def build_layout(lst,cols):
    array = []
    for i in range(0, len(lst), cols):
        array.append(lst[i:i+cols])
        
    return array


def product_list(request):
   
    search_querry = request.GET.get("search", None)
    if search_querry:
        products = Product.objects.filter(title__icontains=search_querry)
    else:
        products = Product.objects.all()
    categories = Category.objects.all()
    return render(request, "store/index.html", context={"product_list": build_layout(products, 3), "cats": categories})
    

def product_detail(request, pk):
    product = Product.objects.get(pk = pk) 
    categories = Category.objects.all()
    return render(request, "store/product_detail.html", context={"product": product, "cats": categories})
    
def category_detail(request, pk):
    categories = Category.objects.all()
    category = Category.objects.get(pk = pk)
    products = category.products.all()
    return render(request, "store/category_detail.html", context={"cats": categories, "product_list": build_layout(products, 3), "category": category})
    

def save_order(request):
    order = Order()
    categories = Category.objects.all()
    order.name = request.POST['user_name']
    order.tel = request.POST["user_phone"]
    order.product = Product.objects.get(pk = request.POST["product_id"])
    order.save()
    return render(request, "store/save_order.html", context={"order": order, "cats": categories})




