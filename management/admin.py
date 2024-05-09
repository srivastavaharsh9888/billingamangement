from django.contrib import admin
from django.contrib.auth.models import User, Group
from django.contrib.admin import AdminSite

from .models import Product, Bill, BillProduct

admin.site.unregister(User)
admin.site.unregister(Group)


class MyAdminSite(AdminSite):
    site_header = 'Billing Management'
    site_title = 'Billing Admin Portal'
    index_title = 'Hey, Admin you can add your product and bills here'


admin_site = MyAdminSite(name='myadmin')


@admin.register(Product, site=admin_site)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'description']
    search_fields = ['name']


class BillProductInline(admin.TabularInline):
    model = BillProduct
    extra = 1
    readonly_fields = ['buying_price']  # Prevent the admin from editing the buying price

    def save_formset(self, request, form, formset, change):
        instances = formset.save(commit=False)
        for instance in instances:
            if isinstance(instance, BillProduct):  # Check if it's a BillProduct instance
                instance.buying_price = instance.product.price  # Set buying price to current product price
                instance.save()
        formset.save_m2m()
        super().save_formset(request, form, formset, change)


@admin.register(Bill, site=admin_site)
class BillAdmin(admin.ModelAdmin):
    inlines = [BillProductInline]
    list_display = ['id', 'total_cost']
    readonly_fields = ['total_cost']  # Total cost should also be read-only

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        print(BillProduct.objects.filter(bill=obj))
        print(bp.buying_price for bp in BillProduct.objects.filter(bill=obj))
        obj.total_cost = sum(bp.buying_price for bp in BillProduct.objects.filter(bill=obj))
        obj.save()
