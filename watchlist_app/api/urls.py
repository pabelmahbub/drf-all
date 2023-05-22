from django.urls import path, include
# for Functiona views(chagne only in urls.py and views.py):

# from watchlist_app.api.views import movie_list, movie_details
#urlpatterns = [
#    path('list/', movie_list, name= "movie_list"),
#    path('<int:pk>', movie_details, name= "movie_detail"),



# for Class views(chagne only in urls.py and views.py):
from watchlist_app.api.views import MovieListAV, MovieDetailsAV

urlpatterns = [
    path('list/', MovieListAV.as_view(), name= "movie_list"),
    path('<int:pk>', MovieDetailsAV.as_view(), name= "movie_detail"),
]