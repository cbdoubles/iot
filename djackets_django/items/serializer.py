from rest_framework import serializers

from .models import Product

class ItemSerializer(serializers.ModelSerializer):
    class Meta: #used to configure this
        model = Product
        fields = ( #fields that we're going to use in the front end
            "id",
            "title",
            "get_absolute_url",
            "description",
            "get_image",
            "get_thumbnail"
        )
        