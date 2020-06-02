from django.shortcuts import render, redirect 
from .models import Order, Product

def index(request):
    context = {
        "all_products": Product.objects.all()
    }
    return render(request, "store/index.html", context)

def checkout(request):
    quantity_from_form = int(request.POST["quantity"])
    price_from_form = float(request.POST["price"])
    total_charge = quantity_from_form * price_from_form
    Order.objects.create(quantity_ordered=quantity_from_form, total_price=total_charge)
    quantity = Order.objects.aggregate(Sum("quantity_ordered"))
    total_spend = Order.objects.aggregate(Sum("total_price"))
    context={
        "total": total_charge,
        "quantity": quantity,
        "total_spend": total_spend,
    }
    return render(request, "store/checkout.html")