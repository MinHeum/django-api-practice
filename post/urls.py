from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# django rest framework -> router -> urls

router = DefaultRouter()
router.register('post', views.PostViewSet) # view를 바탕으로 router resister 를 set하겠다는 뜻

urlpatterns = [
    path('', include(router.urls)),
]
