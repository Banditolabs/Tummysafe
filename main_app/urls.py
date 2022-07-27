from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_places, name='home'),
    path('accounts/signup/', views.signup, name='signup'),
    # read
    path('places/', views.all_places, name='all_places'),
    path('places/my_places', views.user_places, name='user_places'),
    path('places/<int:place_id>/', views.places_detail, name='places_detail' ),
    path('places/<int:place_id>/add_review/', views.add_review, name='add_review'),
    # create
    path('places/create', views.PlaceCreate.as_view(), name='places_create'),
    # update
    path('places/<int:pk>/update/', views.PlaceUpdate.as_view(), name='places_update'),
    # delete
    path('places/<int:pk>/delete/', views.PlaceDelete.as_view(), name='places_delete'),
    path('places/<int:place_id>/add_photo', views.add_photo, name='add_photo')

]
