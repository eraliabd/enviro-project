from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def product(request):
    return render(request, 'Assets/products.html')


def media(request):
    return render(request, 'Assets/media.html')


def building(request):
    return render(request, 'Assets/building.html')


def building_data(request):
    return render(request, 'Assets/buildingData.html')


def contact(request):
    return render(request, 'Assets/contacts.html')
