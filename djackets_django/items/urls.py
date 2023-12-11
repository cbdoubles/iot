from django.urls import path, include

from items import views

urlpatterns = [
    path('latest-products/', views.LatestProductsList.as_view()),
    path('createNew', views.enterProduct.as_view()),
    path('latest-products/<str:dbox_id>/', views.DBoxProductsList.as_view()),
    path('api/create-product/', views.CreateProduct.as_view(), name='create_product'),
    path('products/<slug:item_slug>/<slug:product_slug>/', views.ProductDetail.as_view()),
    
    #info received from tablet
    path('check-free-box/', views.CheckAvailableBox.as_view(), name='check_free_box'),
    path('api/delete-product/', views.DeleteProduct.as_view(), name='delete_product'),
]
#need to import this to the other urls in main folder