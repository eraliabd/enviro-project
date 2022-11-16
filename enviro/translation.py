from modeltranslation.translator import translator, register, TranslationOptions
from .models import Main, Product, ProductCategory, WhyUs, Contact, Media


@register(ProductCategory)
class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'text')


# @register(WhyUs)
# class NewsTranslationOptions(TranslationOptions):
#     fields = ('title_en', 'text')
#
#
# @register(Product)
# class NewsTranslationOptions(TranslationOptions):
#     fields = ('title', 'text')
#
# @register(Contact)
# class NewsTranslationOptions(TranslationOptions):
#     fields = ('title', 'text')
#
#
# @register(Media)
# class NewsTranslationOptions(TranslationOptions):
#     fields = ('title', 'text')
#
#
# @register(Main)
# class NewsTranslationOptions(TranslationOptions):
#     fields = ('title', 'text')

# translator.register(NewsTranslationOptions)
