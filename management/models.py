from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=500)
    description = models.TextField()
    price = models.FloatField()

    def __str__(self):
        return f"Product - #{self.id} - ${self.name}(Rs{self.price})"

class Bill(models.Model):
    products = models.ManyToManyField(Product, through='BillProduct', related_name='bills')
    total_cost = models.FloatField(editable=False, default=0.0)  # Make total_cost non-editable

class BillProduct(models.Model):
    bill = models.ForeignKey(Bill, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    buying_price = models.FloatField()

    def __str__(self):
        return f"{self.product.name} at ${self.buying_price}"