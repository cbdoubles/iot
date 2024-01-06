from rest_framework import serializers

from .models import Product

class ItemSerializer(serializers.ModelSerializer):
    
    box_id = serializers.CharField(source='get_box_property', read_only=True)
    box_number = serializers.IntegerField(source='get_box_num', read_only=True)
    
    class Meta: #used to configure this
        model = Product
        fields = ( #fields that we're going to use in the front end
            # "id",
            "box_id",
            "box_number",
            "title",
            # "get_absolute_url",
            "description",
            "get_image",
            "get_thumbnail",
        )
        