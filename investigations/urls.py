from django.urls import path
from .views import xpto
urlpatterns = [
    path('xpto/', view=xpto.as_view(), name="xpto")
]