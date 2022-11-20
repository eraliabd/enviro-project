from django.db import models
from ckeditor.fields import RichTextField


class Main(models.Model):
    # main
    # title = RichTextField(max_length=255, null=True, blank=True)
    title = models.CharField(max_length=255, null=True, blank=True)
    text = models.TextField(null=True, blank=True)

    # about us
    about_title = models.CharField(max_length=255, null=True, blank=True)
    about_text = models.TextField(null=True, blank=True)

    # contact
    contact_title = models.CharField(max_length=255, null=True, blank=True)
    contact_text = models.TextField(null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(max_length=70, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Main'


class Contact(models.Model):
    full_name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(max_length=70)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name


class Logo(models.Model):
    logo_image = models.ImageField(upload_to='logo_img')

    def __str__(self):
        return self.logo_image


class WhyUs(models.Model):
    image = models.ImageField(upload_to='why_us_img')
    title = models.CharField(max_length=255)
    text = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Why Us'


class Media(models.Model):
    image = models.ImageField(upload_to='media_img')
    title = models.CharField(max_length=255)
    text = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Media'


class ProductCategory(models.Model):
    image = models.ImageField(upload_to='category_img')
    title = models.CharField(max_length=255)
    text = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Product Categories'


class Product(models.Model):
    product_category = models.ForeignKey(ProductCategory, null=True, on_delete=models.SET_NULL, related_name='category')
    image = models.ImageField(upload_to='product_img')
    title = models.CharField(max_length=255)
    text = models.TextField()

    shape = models.CharField(max_length=50)
    weight = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    packing_specification = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.title}"


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='product')
    full_name = models.CharField(max_length=200, null=True)
    phone_number = models.CharField(max_length=20, null=True)
    email = models.EmailField(max_length=70, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"The product ordered by {self.full_name}"

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'


