from django.shortcuts import render, get_object_or_404
from .models import Main, Product, ProductCategory, WhyUs, Contact, Logo, Media


def index(request):
    main = Main.objects.get()
    categories = ProductCategory.objects.all()
    why_us = WhyUs.objects.all()
    why_content1 = why_us[:2]
    why_content2 = why_us[2:]
    # print(why_content1)
    # print(why_content2)
    logos = Logo.objects.all()

    context = {
        'mains': main,
        'why_content1': why_content1,
        'why_content2': why_content2,
        'logos': logos,
        'categories': categories,
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
    first_media = medias[:2]
    second_media = medias[2:]

    context = {
        'first_media': first_media,
        'second_media': second_media,
    }

    return render(request, 'Assets/media.html', context)


def building(request, pk):
    buildings = Product.objects.filter(product_category_id=pk)

    context = {
        'buildings': buildings,
    }
    return render(request, 'Assets/building.html', context)


def building_data(request, pk):
    buildings = Product.objects.filter(product_category_id=pk)
    building_data = get_object_or_404(Product, id=pk)

    context = {
        'building_data': building_data,
        'buildings': buildings,
    }
    return render(request, 'Assets/buildingData.html', context)


def contact(request):
    return render(request, 'Assets/contacts.html')
