from django.urls import path, include
from rest_framework.routers import DefaultRouter
from watchlist_app.api import views
# for Functional views(chagne only in urls.py and views.py):

# from watchlist_app.api.views import movie_list, movie_details
#urlpatterns = [
#    path('list/', movie_list, name= "movie_list"),
#    path('<int:pk>', movie_details, name= "movie_detail"),



# for Class views(chagne only in urls.py and views.py):
from watchlist_app.api.views import WatchListAV, WatchListDetailAV, StreamPlatformAV, StreamPlatformDetailAV, ReviewCreate, ReviewList, ReviewDetail


# router = DefaultRouter()
# router.register('stream/', views.StreamPlatformVS, basename='streamplatform')


urlpatterns = [
    path('list/', WatchListAV.as_view(), name= "movie_list"),
    path('list/<int:pk>/', WatchListDetailAV.as_view(), name= "movie_detail"),
    
    path('stream/', StreamPlatformAV.as_view(), name= "stream_list"),
    path('stream/<int:pk>/', StreamPlatformDetailAV.as_view(), name= "stream_detail"),
    
    path('<int:pk>/review-create/', ReviewCreate.as_view(), name= "review-create"),
    path('<int:pk>/reviews/', ReviewList.as_view(), name= "review-list"),
    path('review/<int:pk>/', ReviewDetail.as_view(), name= "review-detail"),
    
    #for review model mixins:
    # path('review', ReviewList.as_view(), name= "review_list"),
    # path('review/<int:pk>', ReviewDetail.as_view(), name= "review_detail"),
]