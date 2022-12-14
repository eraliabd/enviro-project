from django.shortcuts import render, redirect, get_object_or_404
from django.utils.translation import gettext as _
from .models import Main, Product, ProductCategory, WhyUs, Contact, Logo, Media, Order, SocialNetwork


def index(request):
    main = Main.objects.get()
    categories = ProductCategory.objects.all()
    social_networks = SocialNetwork.objects.get()
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
        'social_networks': social_networks,
    }
    return render(request, 'index.html', context)


def product(request):
    products = ProductCategory.objects.all()
    social_networks = SocialNetwork.objects.get()

    context = {
        'products': products,
        'social_networks': social_networks,
    }
    return render(request, 'Assets/products.html', context)


def media(request):
    medias = Media.objects.all()
    first_media = medias[:len(medias) // 2]
    second_media = medias[len(medias) // 2:]
    social_networks = SocialNetwork.objects.get()

    context = {
        'first_media': first_media,
        'second_media': second_media,
        'social_networks': social_networks,
    }

    return render(request, 'Assets/media.html', context)


def building(request, pk):
    buildings = Product.objects.filter(product_category_id=pk)
    buildings1 = buildings[:len(buildings) // 2]
    buildings2 = buildings[len(buildings) // 2:]
    # print("1: ", buildings)
    # print("2: ", buildings1)
    # print("3: ", buildings2)
    product_category = ProductCategory.objects.all()
    # print(product_category)
    social_networks = SocialNetwork.objects.get()

    context = {
        'buildings1': buildings1,
        'buildings2': buildings2,
        'product_category': product_category,
        'buildings': buildings,
        'social_networks': social_networks,
    }
    return render(request, 'Assets/building.html', context)


def building_data(request, category_id, pk):
    buildings = Product.objects.filter(product_category_id=category_id)
    building_data = get_object_or_404(Product, id=pk)
    social_networks = SocialNetwork.objects.get()

    # print("buildings:", buildings)

    context = {
        'building_data': building_data,
        'buildings': buildings,
        'social_networks': social_networks,
    }
    return render(request, 'Assets/buildingData.html', context)


def contact(request):
    main = Main.objects.get()
    social_networks = SocialNetwork.objects.get()
    if request.method == 'POST':
        model = Contact()
        model.full_name = request.POST.get('name', '')
        model.phone_number = request.POST.get('phone_number', '')
        model.email = request.POST.get('email', '')

        model.save()
        return redirect('enviro:success')

    context = {
        'main': main,
        'social_networks': social_networks,
    }

    return render(request, 'Assets/contacts.html', context)


def order(request, category_id, name, pk):
    social_networks = SocialNetwork.objects.get()
    buildings = Product.objects.filter(product_category_id=category_id)
    building_data = get_object_or_404(Product, id=pk)
    categories = ProductCategory.objects.all()

    if request.method == 'POST':
        model = Contact()
        model.full_name = request.POST.get('name', '')
        model.phone_number = request.POST.get('phone_number', '')
        model.email = request.POST.get('email', '')

        order = Order(
            product_id=pk,
            full_name=model.full_name,
            phone_number=model.phone_number,
            email=model.email,
        )

        order.save()
        return redirect('enviro:order_success')

    context = {
        'building_data': building_data,
        'buildings': buildings,
        'categories': categories,
        'social_networks': social_networks,
    }
    return render(request, 'Assets/order.html', context)


def success(request):
    main = Main.objects.get()
    social_networks = SocialNetwork.objects.get()
    print("main:", main)

    context = {
        'main': main,
        'social_networks': social_networks,
    }

    return render(request, 'Assets/success.html', context)


def order_success(request):
    social_networks = SocialNetwork.objects.get()
    buildings = Product.objects.all()[:2]
    building_data = get_object_or_404(Product.objects.all()[:1])
    categories = ProductCategory.objects.all()

    context = {
        'building_data': building_data,
        'buildings': buildings,
        'categories': categories,
        'social_networks': social_networks,
    }
    return render(request, 'Assets/order_success.html', context)
