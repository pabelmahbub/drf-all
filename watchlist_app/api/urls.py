from django.urls import path, include
# for Functiona views(chagne only in urls.py and views.py):

# from watchlist_app.api.views import movie_list, movie_details
#urlpatterns = [
#    path('list/', movie_list, name= "movie_list"),
#    path('<int:pk>', movie_details, name= "movie_detail"),



# for Class views(chagne only in urls.py and views.py):
from watchlist_app.api.views import WatchListAV, WatchListDetailAV, StreamPlatformAV, StreamPlatformDetailAV, ReviewCreate, ReviewList, ReviewDetail

urlpatterns = [
    path('list/', WatchListAV.as_view(), name= "movie_list"),
    path('<int:pk>', WatchListDetailAV.as_view(), name= "movie_detail"),
    
    path('stream/', StreamPlatformAV.as_view(), name= "stream_list"),
    path('stream/<int:pk>', StreamPlatformDetailAV.as_view(), name= "stream_detail"),
    
    path('stream/<int:pk>/review-create', ReviewCreate.as_view(), name= "review-create"),
    path('stream/<int:pk>/review', ReviewList.as_view(), name= "review-list"),
    path('stream/review/<int:pk>', ReviewDetail.as_view(), name= "review-detail"),
    
    #for review model mixins:
    # path('review', ReviewList.as_view(), name= "review_list"),
    # path('review/<int:pk>', ReviewDetail.as_view(), name= "review_detail"),
]