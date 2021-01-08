from django.contrib import admin
from PSI.models import Product
from PSI.models import Order
from PSI.core import core
from PSI.core import css as util
# Register your models here.
from .models import *

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'css')
    actions = ['update_css']

    def update_css(self, request, queryset):
        for cust in queryset:
            order_list = Order.objects.filter(complete=True).filter(customer = cust)
            print(order_list)
            used_order_list = order_list.filter(used = True)
            unused_order_list = order_list.filter(used = False)
            total_psi = 0
            order_cnt = len(used_order_list)
            for order in used_order_list:
                total_psi += order.Average_PSS
            avg_psi = 0
            if order_cnt > 0:
                avg_psi = total_psi / order_cnt
            tcss = cust.css
            for order in unused_order_list:
                tcss = util.get_css(tcss, avg_psi, order_cnt, order.Average_PSS)
                total_psi += order.Average_PSS
                order_cnt += 1
                avg_psi = total_psi / order_cnt
                order.used = True
                order.save()
            cust.css = tcss
            cust.save()

admin.site.register(Customer, CustomerAdmin)
#admin.site.register(Product)
class OrderAdmin(admin.ModelAdmin):
    readonly_fields = ('date_ordered',)
    list_display = ('customer','used')
admin.site.register(Order,OrderAdmin)

class OrderItemAdmin(admin.ModelAdmin):
    readonly_fields = ('date_added',)
admin.site.register(OrderItem,OrderItemAdmin)

class ShippingAddressAdmin(admin.ModelAdmin):
    readonly_fields = ('date_added',)
admin.site.register(ShippingAddress,ShippingAddressAdmin)
#admin.site.register(Unprocessed_item)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','pss','listed')
    actions = ['list_items', 'unlist_items']

    def list_items(self, request, queryset):
        g = core.generator(0,15,0,50,0,2,0,10)
        g.start()

        q1 = queryset.filter(listed='n')
        for item in q1:
            item.pss = g.get_psi(
                item.carbon_footprint,
                item.recyclability,
                item.water_used,
                item.energy
            )
            item.listed = 'y'
            item.save()

        """
        self.message_user(request, ngettext(
            '%d product was successfully marked as listed.',
            '%d stories were successfully marked as listed.',
            q1,
        ) % q1, messages.SUCCESS)
        """

    def unlist_items(self, request, queryset):
        for item in queryset:
            item.listed = 'n'
            item.pss = 0
            item.save()

    list_items.short_description = "List unlisted items"
    unlist_items.short_description = "Unlist selected items"

admin.site.register(Product,ProductAdmin)

