from django.urls import path
from profiles_api import views

urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view())           #just as in urls.py from profiles_project   .as_view() - std function call for HelloApiView to be rendered by URL
]
