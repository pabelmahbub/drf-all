#A. Model serializer

from rest_framework import serializers
from watchlist_app.models import WatchList, StreamPlatform, Review



class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"
class WatchListSerializer(serializers.ModelSerializer):
    movieReviews = ReviewSerializer(many=True, read_only= True)
    class Meta:
        model = WatchList
        fields = '__all__'

class StreamPlatformSerializer(serializers.ModelSerializer):
    #myWatchList same as model related name:
    myWatchList = WatchListSerializer(many=True, read_only=True)
    class Meta:
        model = StreamPlatform
        fields = '__all__'        
  


# B.Serializer.serializers

# from rest_framework import serializers
# from watchlist_app.models import Movie


# def name_length(value):
#     if len(value) < 3:
#             raise serializers.ValidationError("Name must be at least 3 characters long")
        
        
# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(validators=[name_length])
#     description = serializers.CharField()
#     active = serializers.BooleanField()
    
    
    
#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)

    # def update(self, instance, validated_data):
    #     instance.name = validated_data.get('name', instance.name)
    #     instance.description = validated_data.get('description', instance.description)
    #     instance.active = validated_data.get('active', instance.active)
    #     instance.save()
    #     return instance
    
    
    #Extra work: validation methods: are 3 types of validation methods.a.Field level, b)Object level, c)Validator level
    #2.object level validation:
    
    # def validate_name(self, value):
    #     if len(value) < 2:
    #         raise serializers.ValidationError("Name is too short")
    #     else:
    #         return value
     
    #. 1. Field level validation:
    # def validate(self, data):
    #     if data['name'] ==  data['description']:
    #         raise serializers.ValidationError("Title and Description cannot be the same")
    #     else:
    #         return data   
     
    #3.Validator level validation: in top:
