from .views import landing_page
from django.urls import path


app_name = 'home'
urlpatterns = [
    path('', landing_page, name='landing_page'),
]