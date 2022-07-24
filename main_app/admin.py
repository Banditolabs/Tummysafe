from django.contrib import admin

# Register your models here.
from .models import Place, GoldMedal, SilverMedal, BronzeMedal, Profile

admin.site.register(Place)
admin.site.register(GoldMedal)
admin.site.register(SilverMedal)
admin.site.register(BronzeMedal)
admin.site.register(Profile)