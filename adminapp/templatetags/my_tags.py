from django import template
from django.conf import settings

register = template.Library()

def media_folder_products(string):
    """
    products_images/product1.jpg --> /media/products_images/product1.jpg
    путь добавляем
    """
    if not string:
        string = 'products_images/default.jpg'

    return f'{settings.MEDIA_URL}{string}'


@register.filter(name='media_folder_users')
def media_folder_users(string):
    """
    тож самое только  к юзерам
    """
    if not string:
        string = 'users_avatards/default.jpg'

    return f'{settings.MEDIA_URL}{string}'


register.filter('media_folder_products', media_folder_products)

