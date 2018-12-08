from rest_framework import serializers
from faketinder.models import User
class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
        'bio',
        'name',
        'photos', # a list of photo URLs
        'thumbnail', #a list of thumbnails of photo URLS
        'age', # their age
        'birth_date', # their birth_date
        'ping_time', # last online
        'distance_km', # distane from you
        'common_connections', # friends in common
        'common_interests', # likes in common - returns a list of {'name':NAME, 'id':ID}
        'instagram_username', # instagram username
        'instagram_photos', # a list of instagram photos with these fields for each photo: 'image','link','thumbnail'
        'schools', # list of schools
        'jobs',)
