from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.utils.translation import gettext as _
from django.db.models import Max, Q

from .models import Main, Product, ProductCategory, WhyUs, Contact, Logo, Media, Order
from .forms import ProductForm, OrderForm


def index(request):
    main = Main.objects.get()
    categories = ProductCategory.objects.all()
    why_us = WhyUs.objects.all()
    # print("w: ", why_us)
    # print("w: ", why_us[:2])
    why_content1 = why_us[:len(why_us) // 2]
    why_content2 = why_us[len(why_us) // 2:]
    # print(why_content1)
    # print(why_content2)
    logos = Logo.objects.all()

    if request.method == 'POST':
        model = Contact()
        model.full_name = request.POST.get('name', '')
        model.phone_number = request.POST.get('phone_number', '')
        model.email = request.POST.get('email', '')

        model.save()

    context = {
        'mains': main,
        'why_content1': why_content1,
        'why_content2': why_content2,
        'logos': logos,
        'categories': categories,
        'why_us': why_us,
    }
    return render(request, 'index.html', context)


def product(request):
    products = ProductCategory.objects.all()

    context = {
        'products': products,
    }
    return render(request, 'Assets/products.html', context)


def media(request):
    medias = Media.objects.all()
    first_media = medias[:len(medias) // 2]
    second_media = medias[len(medias) // 2:]

    context = {
        'first_media': first_media,
        'second_media': second_media,
    }

    return render(request, 'Assets/media.html', context)


def building(request, pk):
    buildings = Product.objects.filter(product_category_id=pk)
    buildings1 = buildings[:len(buildings) // 2]
    buildings2 = buildings[len(buildings) // 2:]
    # print("1: ", buildings)
    # print("2: ", buildings1)
    # print("3: ", buildings2)
    products = ProductCategory.objects.all()

    context = {
        'buildings1': buildings1,
        'buildings2': buildings2,
        'products': products,
        'buildings': buildings,
    }
    return render(request, 'Assets/building.html', context)


def building_data(request, pk):
    buildings = Product.objects.filter(product_category_id=pk)
    building_data = get_object_or_404(Product, id=pk)
    categories = ProductCategory.objects.filter()

    # print(buildings)

    context = {
        'building_data': building_data,
        'buildings': buildings,
        'categories': categories,
    }
    return render(request, 'Assets/buildingData.html', context)


def contact(request):
    main = Main.objects.get()
    if request.method == 'POST':
        model = Contact()
        model.full_name = request.POST.get('name', '')
        model.phone_number = request.POST.get('phone_number', '')
        model.email = request.POST.get('email', '')

        model.save()

    context = {
        'main': main
    }

    return render(request, 'Assets/contacts.html', context)


def order(request, pk):
    buildings = Product.objects.filter(product_category_id=pk)
    building_data = get_object_or_404(Product, id=pk)
    categories = ProductCategory.objects.all()
    product = ProductForm()
    order_form = OrderForm()

    if request.method == 'POST':
        model = Contact()
        model.full_name = request.POST.get('name', '')
        model.phone_number = request.POST.get('phone_number', '')
        model.email = request.POST.get('email', '')

        # model.save()
        # contact = (
        #     Contact.objects.values('id', 'full_name', 'phone_number', 'email').
        #         annotate(count=Max('id')).order_by('-id')[:1]
        # )
        # print(contact)

        order = Order(
            product_id=pk,
            full_name=model.full_name,
            phone_number=model.phone_number,
            email=model.email,
        )

        order.save()

    context = {
        'building_data': building_data,
        'buildings': buildings,
        'categories': categories,
    }
    return render(request, 'Assets/order.html', context)


def success(request):
    main = Main.objects.get()

    context = {
        'main': main
    }

    return render(request, 'Assets/success.html', context)
