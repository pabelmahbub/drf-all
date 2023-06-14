from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from user_app.models import MovieOne
from user_app.api.serializers import MovieOneSerializer

@api_view(['GET', 'POST'])
def movie_list(request):
    if request.method == 'GET':
        movies = MovieOne.objects.all()
        serializer = MovieOneSerializer(movies, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = MovieOneSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
   
@api_view(['GET', 'PUT','DELETE'])
def movie_details(request, pk):
    if request.method == 'GET':
        try:
             movieOne = MovieOne.objects.get(pk=pk)
        except MovieOne.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)  
           
        serializer = MovieOneSerializer(movieOne)
        return Response(serializer.data)
    
    if request.method == 'PUT':
        movieOne = MovieOne.objects.get(pk=pk)
        serializer = MovieOneSerializer(movieOne, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    if request.method == 'DELETE':
        movieOne = MovieOne.objects.get(pk=pk)
        movieOne.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)