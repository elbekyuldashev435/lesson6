from django.urls import path
from .views import RegisterView, LoginView
from home.views import landing_page


app_name = 'users'
urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('/home/', landing_page, name='landing_page')
]