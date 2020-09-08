from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name="shopHome"),
    path('about/',views.about,name="about"),
    path('contact/',views.contact,name="contactus"),
    path('search/',views.search,name="search"),
    path('tracker/',views.tracker,name="tracker"),
    path('checkout/',views.checkout,name="checkout"),
    path('productview/<int:prodid>',views.productview,name="prodview")

]
