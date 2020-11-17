from django.urls import path,include
from rest_framework import routers
from .views import *

router=routers.DefaultRouter()
router.register('verify',verifyview,basename='verify')
router.register('quiz',quizview,basename='quiz')

urlpatterns=[
    path('api/',include(router.urls))
]

