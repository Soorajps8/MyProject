from django.urls import path
from webapp import views

urlpatterns=[
    path('home_pg/',views.home_pg,name="home_pg"),
    path('about_us/',views.about_us,name="about_us"),
    path('contact_us/',views.contact_us,name="contact_us"),
    path('cat_pg/',views.cat_pg,name="cat_pg"),
    path('prod_pg/<cat_name>',views.prod_pg,name="prod_pg"),
    path('cart_pg/',views.cart_pg,name="cart_pg"),
    path('singleproductpage/<int:dataid>/',views.singleproductpage,name="singleproductpage"),
    path('registrationpage/',views.registrationpage,name="registrationpage"),
    path('user_register/',views.user_register,name="user_register")
]
