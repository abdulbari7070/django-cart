from xml.etree.ElementInclude import include
from rest_framework import routers
from django.urls import path, include
from category import views

router = routers.DefaultRouter()
router.register(r'category', views.CategoryViewSet,basename="categories")

urlpatterns = [
    path('', include(router.urls)),
]
