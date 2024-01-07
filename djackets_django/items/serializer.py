from rest_framework import serializers

from .models import Product, Box

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


class CreateItemSerializer(serializers.ModelSerializer):
    box_uid = serializers.CharField(write_only=True)

    class Meta:
        model = Product
        fields = (
            "box_uid",
            "title",
            "description",
            "get_image",
        )

    def create(self, validated_data):
        # Extract and remove 'box_uid' from validated_data
        box_uid = validated_data.pop('box_uid')

        # Get the Box instance using the unique_ID
        box = Box.objects.get(unique_ID=box_uid)

        # Create the Product instance with the associated Box
        product = Product.objects.create(box=box, **validated_data)

        return product
        