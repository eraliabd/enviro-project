from modeltranslation.translator import translator, register, TranslationOptions
from .models import Main, Product, ProductCategory, WhyUs, Contact, Media


@register(ProductCategory)
class ProductCategoryTranslationOptions(TranslationOptions):
    fields = ('title', 'text')


@register(WhyUs)
class WhyUsTranslationOptions(TranslationOptions):
    fields = ('title', 'text')


@register(Media)
class MediaTranslationOptions(TranslationOptions):
    fields = ('title', 'text')


@register(Main)
class MainTranslationOptions(TranslationOptions):
    fields = ('title', 'text', 'about_title', 'about_text', 'contact_title', 'contact_text')

# @register(Product)
# class ProductTranslationOptions(TranslationOptions):
#     fields = ('title', 'text')

# translator.register(NewsTranslationOptions)
