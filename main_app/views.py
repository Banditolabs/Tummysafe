from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Place, User, Photo
from .forms import ReviewForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import UserPassesTestMixin

import uuid, boto3
S3_BASE_URL = 'https://s3-us-west-2.amazonaws.com/'
BUCKET = 'tummysafe'
# Create your views here.

# views for the Place class

class PlaceCreate(LoginRequiredMixin,CreateView):
  model = Place
  fields = ['name', 'postcode', 'address_line', 'address_line2', 'state_province', 'town_city', 'health_rating', 'service_rating', 'taste_rating']

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)


class PlaceUpdate(LoginRequiredMixin, UpdateView):
  model = Place
  fields = ['name', 'postcode', 'address_line', 'address_line2', 'state_province', 'town_city', 'health_rating', 'service_rating', 'taste_rating']
# UserPassesTestMixin
  # def test_func(self):
  #   return self.request.user.id == self.request


class PlaceDelete(LoginRequiredMixin,DeleteView):
  model = Place
  success_url = '/places/'

@login_required
def places_detail(request, place_id):
  place = Place.objects.get(id=place_id)
  review_form = ReviewForm()
  return render(request, 'places/details.html', {'place': place, 'review_form': review_form})

@login_required
def user_places(request):
    places = Place.objects.filter(user=request.user)
    return render(request, 'places/my_places.html', {'places': places})


def all_places(request):
  places = Place.objects.all().order_by('-id')
  return render(request, 'places/index.html', {'places': places})

# Utility views
def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('all_places')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form':form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)

@login_required
def add_photo(request, place_id):
  photo_file = request.FILES.get('photo-file', None)
  if photo_file:
    s3 = boto3.Session(profile_name='tummysafe').client('s3')
    key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
    try:
      s3.upload_fileobj(photo_file, BUCKET, key)
      url = f"{S3_BASE_URL}{BUCKET}/{key}"
      photo = Photo(url=url, place_id=place_id)
      photo.save()
    except:
      print('An error occurred uploading file to S3')
  return redirect('places_detail', place_id=place_id)

@login_required
def add_review(request, place_id):
  form = ReviewForm(request.POST)
  if form.is_valid():
    new_review = form.save(commit=False)
    new_review.place_id = place_id
    new_review.save()
  return redirect('places_detail', place_id=place_id)