from django.urls import path
from .views import *

urlpatterns = [
    path('schools/', SchoolList.as_view()),
    # path('api/schools/<int:pk>/', views.SchoolDetail.as_view()),
]