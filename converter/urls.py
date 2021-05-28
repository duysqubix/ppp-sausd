from django.urls import path
from converter import views

urlpatterns = [
    path("", views.main_view, name="main_view")
]
