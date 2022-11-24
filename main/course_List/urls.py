from django.urls import path
from . import views
urlpatterns = [
    path("", views.main, name = "main"),
    path("<str:name>", views.personalized_main, name = "p_main")
]
