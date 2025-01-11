from django.urls import path
from .views import NovelList

urlpatterns = [
    path('novels/', NovelList.as_view(), name='novel-list'),
]
