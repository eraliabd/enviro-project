from modeltranslation.translator import translator, TranslationOptions
from .models import ProductCategory


class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'text')


translator.register(ProductCategory, NewsTranslationOptions)
