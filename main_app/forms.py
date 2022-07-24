from django.forms import ModelForm
from .models import Review

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['content', 'health_rating', 'service_rating', 'taste_rating']