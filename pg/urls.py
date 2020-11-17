from django.urls import path,include
from rest_framework import routers
from .views import *

router=routers.DefaultRouter()
router.register('pgowner',pgownerView,basename='pgowner')


urlpatterns=[
    path('api/v3/',include(router.urls)), 
]
