from myapp.views import *

from django.urls import path

urlpatterns = [
    path('product/', product),
    path('freprod/', frequent_products),

]