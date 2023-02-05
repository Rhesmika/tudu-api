from django.urls import path
from teams import views

urlpatterns = [
    path('teams/', views.TeamList.as_view()),

]
