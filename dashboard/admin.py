from django.contrib import admin
from .models import CountryData

class CountryAdmin(admin.ModelAdmin):
  # fields = ['name', 'title', 'contents', 'url', 'email', 'owner']
  list_display = ('country', 'population',)
  list_filter = ['population']
  search_fields = ['country',]
  fieldsets = [
    ('국가' , {'fields': ['country']}), 
    ('인구', {'fields':['population']}), 
  ]

# Register your models here.
admin.site.register(CountryData, CountryAdmin)