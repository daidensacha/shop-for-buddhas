from django.db import models
from django.conf import settings

""" Product ratings for the product rating select field """
product_rating = (('1', '1/5 stars'),
                  ('2', '2/5 stars'),
                  ('3', '3/5 stars'),
                  ('4', '4/5 stars'),
                  ('5', '5/5 stars')
                  )


class Category(models.Model):
    """ Model for the shop product categories """

    class Meta:
        """ Plural name for the Category model in the admin view """

        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    """ Model for the shop products """

    category = models.ForeignKey('Category', null=True, blank=True,
                                 on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    size = models.CharField(max_length=25, null=True, blank=True)
    color = models.CharField(max_length=25, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.CharField(
                max_length=30, choices=product_rating, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, verbose_name='vendor',
        on_delete=models.CASCADE)
    favorites = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name='favorite',
        default=None, blank=True)

    def __str__(self):
        return self.name
