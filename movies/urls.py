from django.urls import path, include
from .views import Movielistview, MoviedeatilView

urlpatterns = [
    path('', Movielistview.as_view(), name='movie-list'),
    path("movie/detail/<int:pk>",MoviedeatilView.as_view(), name="movie_detail"), 
]