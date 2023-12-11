from django.shortcuts import render, redirect
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
from .serializer import ItemSerializer #tell django what we will get from this model
from .models import Product, DBox, Box

#imports for Create Product
from django.utils import timezone
from django.utils.text import slugify
from rest_framework import status

import os  # Import the os module to manage file operations when deleting photos


### TO BE IMPLEMENTED - view returning TRUE, FALSE for user ###

### PICK-UP ITEMS ###

class DBoxProductsList(APIView):
    def get(self, request, dbox_id, format=None):
        try:
            dbox = DBox.objects.get(unique_ID=dbox_id)
            boxes_in_dbox = dbox.box_set.all()  # Get all boxes related to the DBox
            products_in_dbox = Product.objects.filter(box__in=boxes_in_dbox)
            
            serializer = ItemSerializer(products_in_dbox, many=True)
            return Response(serializer.data)
        except DBox.DoesNotExist:
            return Response({"error": "DBox does not exist"}, status=404)

class ProductDetail(APIView):
    def get_object(self, item_slug, product_slug):
        try:
            return Product.objects.filter(item__slug=item_slug).get(slug=product_slug) #filter any product inside category
        except Product.DoesNotExist:
            raise Http404
        
    def get(self, request, item_slug, product_slug, format=None):
        item = self.get_object(item_slug, product_slug)
        serializer = ItemSerializer(item)
        return Response(serializer.data)

class boxItems(APIView):
    class ProductDetail(APIView):
        def get_object(self, item_slug, dbox_slug):
            try:
                return Product.objects.filter(item__slug=item_slug).get(slug=dbox_slug) #filter any product inside category
            except Product.DoesNotExist:
                raise Http404
        def get(self, request, item_slug, product_slug, format=None):
            item = self.get_object(item_slug, product_slug)
            serializer = ItemSerializer(item)
            return Response(serializer.data)

class DeleteProduct(APIView):
    def post(self, request, format=None):
            # Assuming you are sending DBox ID and Box ID in the request data
            dbox_id = request.data.get('dbox_id')
            box_id = request.data.get('box_id')

            # Get product from box
            dbox = DBox.objects.get(id=dbox_id)
            box = Box.objects.get(id=box_id, dbox=dbox)
            product = Product.objects.get(box=box)
            
            if product.image:
                os.remove(product.image.path)  # Delete the main image file
            if product.thumbnail:
                os.remove(product.thumbnail.path)  # Delete the thumbnail file


            # Delete the product and return confirmation
            product.delete()
            box.isFree = True
            box.save()
            return Response({'message': 'Product deleted successfully'}, status=status.HTTP_200_OK)



### DONATE PRODUCT ###

class CheckAvailableBox(APIView):
    def get(self, request, format=None):
        # Find the first available box
        free_box = Box.objects.filter(isFree=True).first()

        if free_box:
            return Response({'box_num': free_box.box_num}, status=status.HTTP_200_OK)
        else:
            return Response({'box_num': -1}, status=status.HTTP_200_OK)

class CreateProduct(APIView):
    def post(self, request, format=None):
        # Create product after receiving title, description, image, and box_id in the request data
        data = request.data

        # Automatically fill certain fields
        data['date_added'] = timezone.now()
        data['slug'] = slugify(data['title'])

        # Assuming you have a serializer to validate and create the Product instance
        serializer = ItemSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            box_id = data.get('box_id')
            box = Box.objects.get(id=box_id)
            box.isFree = False
            box.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


### TESTING/ IMPLEMENT LATER ###
class LatestProductsList(APIView):
    def get(self, request, format=None):
        items = Product.objects.all()
        serializer = ItemSerializer(items, many=True) #convert this using Product serialise
        return Response(serializer.data)
    #want a serparate url file inside items to keep things tidy