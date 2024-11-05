from django.urls import path ,include  
from . import views
# from .views import api_home


urlpatterns = [
    path('', views.api_home), # localhost:8000/api/
    path('tasks/', include('tasks.urls')),
]