from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Place, User
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm


# Create your views here.

def home(request):
  return render(request, 'home.html')


class PlaceCreate(CreateView):
  model = Place
  fields = ['name', 'address', 'GPS', 'aggregate']
  
  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

def user_places(request):
    places = User.objects.places.filter(user=request.user)
    return render(request, 'places/my_places.html', {'places': places})

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form':form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)