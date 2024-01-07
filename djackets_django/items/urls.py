from django.urls import path, include

from items import views

urlpatterns = [
    path('latest-products/', views.LatestProductsList.as_view()),
    # path('createNew', views.enterProduct.as_view()),
    path('latest-products/<str:dbox_id>/', views.DBoxProductsList.as_view()),
    path('create-product/', views.CreateProduct.as_view(), name='create_product'),
    # path('products/<slug:item_slug>/<slug:product_slug>/', views.ProductDetail.as_view()),
    path('boxes/product/<slug:box_unique_id>/', views.ProductDetail.as_view(), name='product-detail'),
    
    #info received from tablet
    path('check-free-box/', views.CheckAvailableBox.as_view(), name='check_free_box'),
    path('delete-product/', views.DeleteProduct.as_view(), name='delete_product'),
    path('check_user_exists/', views.CheckUserExists.as_view(), name='check_user_exists'),
]
#need to import this to the other urls in main folder
