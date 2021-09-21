from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="Home"),
    # path("<str:sname>", views.user, name="User"),
    path("user/<int:id>", views.index, name="Index"),
    path("create/", views.create, name="Create")
]
