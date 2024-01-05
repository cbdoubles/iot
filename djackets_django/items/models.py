from django.db.models.signals import pre_delete
from django.dispatch import receiver
from django.db import models
from django.core.files import File #import so it is easier to correct thumbnails

from io import BytesIO ## these two are to deal with pictures
from PIL import Image
import uuid #to create uuid


### USER DATABASE ###

class User(models.Model):
    unique_ID = models.CharField(max_length=100, null=True, blank=True, unique=True, default=uuid.uuid4())
    nfc_number = models.CharField(max_length=100, null=True, blank=True, unique=True, default=uuid.uuid4())
    name = models.TextField(verbose_name=("title"), help_text=("Required"))
    products_taken = models.IntegerField(default=0)
    
    def __str__(self): 
        return self.unique_ID

### TESTING/ IMPLEMENT LATER
class Category(models.Model):
    title = models.TextField(verbose_name=("title"), help_text=("Required"))
    #description = models.TextField(verbose_name=("description"), help_text=("Not Required"), blank=True)
    slug = models.SlugField()
    
    class Meta:
        ordering = ('title',) #order cateogry by title in backend
        
    def __str__(self): #show name of category rather than as object in admin iface
        return self.title
    
    def get_absolute_url(self): #get the url for item so it's easier to use in frontend
        return f'/{self.slug}/'

class DBox(models.Model):
    unique_ID = models.CharField(max_length=100, null=True, blank=True, unique=True, default=uuid.uuid4())
    
    def __str__(self): 
        return self.unique_ID
    
class Box(models.Model):
    unique_ID = models.CharField(max_length=100, null=True, blank=True, unique=True, default=uuid.uuid4())
    box_num = models.IntegerField()
    # slug = models.SlugField()
    isFree = models.BooleanField(default=True)
    dbox = models.ForeignKey(DBox, on_delete=models.CASCADE)
    
    def __str__(self): 
        return self.unique_ID
    
    #addProduct 
class Product(models.Model):
    unique_ID = models.CharField(max_length=100, null=True, blank=True, unique=True, default=uuid.uuid4())
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE, blank=True, null=True)
    title = models.TextField(verbose_name=("title"), help_text=("Required"), max_length=255)
    slug = models.SlugField()
    description = models.TextField(verbose_name=("description"), help_text=("Not Required"), blank=True, null=True)
    #can be empty if you don't want a description for certain product
    image = models.ImageField(upload_to='uploads/', blank=True, null=True) #to make mandatory in future
    thumbnail = models.ImageField(upload_to='uploads/', blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    box = models.OneToOneField(Box, default=None, on_delete=models.CASCADE)
    
    class Meta:
        ordering = ('title',) 
        
    def __str__(self): 
        return self.title
    
    def get_absolute_url(self): 
        return f'/{self.slug}/' #get slug based on item field
    
    def get_image(self):
        if self.image:
            return 'http://127.0.0.1:8000' + self.image.url #return whole address so easier to use in frontend
        return '' # return empty string if no image
    
    def get_thumbnail(self):
        if self.thumbnail:
            return 'http://127.0.0.1:8000' + self.thumbnail.url #return url of thumbnail to use in frontend
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image) #if have image, pass in image to thumbnail if one doesn't exist already
                self.save() #so that it is saved in the database
                return 'http://127.0.0.1:8000' + self.thumbnail.url
            return '' # return empty string if no image
        
    def make_thumbnail(self, image, size=(300,200)): #setting thumbnail to image
        img = Image.open(image) #create a new object based on image
        img.convert('RGB')
        img.thumbnail(size) #thumbnail built in function in image
        thum_io = BytesIO()
        img.save(thum_io, 'JPEG', quality=85) #save image
        
        thumbnail = File(thum_io, name=image.name) #create thumbnail using File import
        
        return thumbnail
    

    
    """
    After completing use migration script to update database.
    Beforehand, we need to tell django that this app exists.
    Go to djackets_django -> settings -> INSTALLED_APPS include items to
    inform django about the app and not the model.
    Then input py manage.py makemigrations to want to create
    Then py manage.py migrate to actually create it in database
    """
    
# def delete_product(sender, instance, **kwargs):
#     # When a Product is deleted, update associated Box and DBox
#     if instance.box:
#         box = instance.box
#         dbox = box.dbox

#         # Update Box (set box to None)
#         box.product_set.remove(instance)

#         # Check if the Box is now empty, and update DBox accordingly
#         if box.product_set.count() == 0:
#             box.delete()

#         # Check if the DBox is now empty, and update as needed
#         if dbox.box_set.count() == 0:
#             dbox.delete()