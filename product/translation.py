from modeltranslation.translator import register, translator, TranslationOptions
from .models import Product,Category


class ProductTranslationOptions(TranslationOptions):
    fields = ('variant','title','amount','detail','created_at')


translator.register(Product, ProductTranslationOptions)     



class CategoryTranslationOptions(TranslationOptions):
    fields = ('parent','title','details')

translator.register(Category, CategoryTranslationOptions)  