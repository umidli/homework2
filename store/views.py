from django.shortcuts import render
from .models import Customer

def dashboard(request):
    customers = Customer.objects.all()

    return render(request, "store/index.html", context={"customers": customers})


def create_customer(request):
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    email = request.POST.get('email')
    phone = request.POST.get('phone')
    address = request.POST.get('address')

    if first_name and last_name and email and phone and address:
        customer = Customer(first_name=first_name, last_name=last_name, email=email, phone=phone, address=address)
        customer.save()
        message = f"{customer.first_name} {customer.last_name} ismli mijoz yaratildi!" 
    else:
        message = "mijoz yaratyotganda qatorlarni to'liq to'ldiring!"

    return render(request, "store/create.html", context={"message": message})


