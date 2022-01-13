from django.urls import path, include
from rest_framework.routers import DefaultRouter

from profiles_api import views

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, base_name = 'hello-viewset')

urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),           #just as in urls.py from profiles_project   .as_view() - std function call for HelloApiView to be rendered by URL
    path('', include(router.urls))              #As you register new routes with router, it generates URLs associated for our viewset
]
