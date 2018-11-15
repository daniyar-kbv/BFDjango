from django.urls import path
from . import views
from .views import AdvertList, AdvertDetail

urlpatterns = [
    path('login/', views.login),
    path('register/', views.register),
    path('advert_fbv/', views.advert_list),
    path('advert_fbv/<int:pk>/', views.advert_detail),
    path('advert_cbv/', AdvertList.as_view()),
    path('advert_cbv/<int:pk>/', AdvertDetail.as_view())
]

