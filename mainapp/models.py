from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(verbose_name='название категории', max_length=64, unique=True)
    description = models.TextField(verbose_name='описание категории', blank=True)
    is_active = models.BooleanField(verbose_name='активная категория', default=True)
    
    def __str__(self):
        return self.name

    
class Product(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    name = models.CharField(verbose_name='имя продукта', max_length=128)
    image = models.ImageField(upload_to='products_images', blank=True)
    short_desc = models.CharField(verbose_name='краткое описание продукта', max_length=60, blank=True)
    description = models.TextField(verbose_name='описание продукта', blank=True)
    price = models.DecimalField(verbose_name='цена продукта', max_digits=8, decimal_places=2, default=0)
    quantity = models.PositiveIntegerField(verbose_name='количество на складе', default=0)
    is_active = models.BooleanField(verbose_name='категория активна', default=True)

    # def price_with_discount(self):
    #     discount = 10
    #     result = float(self.price) - float(self.price)*(discount/100)
    #     return result
    #
    # def request(self):
    #     pass

    def __str__(self):
        return "{} ({})".format(self.name, self.category.name)
        