from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('places/', views.all_places, name='all_places'),
    path('places/my_places', views.user_places, name='user_places'),
    path('accounts/signup/', views.signup, name='signup'),
    path('places/<int:place_id>/', views.places_detail, name='places_detail' ),
    path('places/create', views.PlaceCreate.as_view(), name='places_create'),
    path('places/<int:place_id>/add_photo', views.add_photo, name='add_photo')

]
