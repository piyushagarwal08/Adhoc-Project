from django.urls import path
from . import views

urlpatterns = [
        path("",views.index),
        path("महादेव?myvar=41",views.test,name="test"),
        ]

