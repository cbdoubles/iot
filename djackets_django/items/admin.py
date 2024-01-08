from django.contrib import admin

# Register your models here.
from .models import Category, Product, Box, DBox, User

class ProductAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        # Update the associated Box's isFree variable to False
        if obj.box:
            obj.box.isFree = False
            obj.box.save()

        # Call the original save_model method
        super().save_model(request, obj, form, change)

    def delete_model(self, request, obj):
        # Store the associated Box
        box = obj.box

        # Call the original delete_model method to delete the product
        super().delete_model(request, obj)
        box.isFree = True
        box.save()
    

admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(Box)
admin.site.register(DBox)
admin.site.register(User)
