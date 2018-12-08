from django.db import models

# Create your models here.

# class User():
#     bio = models.CharField(max_length=300)# their biography
#     name = models.CharField(max_length=300)# their name
#     photos # a list of photo URLs
#     thumbnail #a list of thumbnails of photo URLS
#     age # their age
#     birth_date # their birth_date
#     ping_time # last online
#     distance_km # distane from you
#     common_connections # friends in common
#     common_interests # likes in common - returns a list of {'name':NAME, 'id':ID}
#     instagram_username # instagram username
#     instagram_photos # a list of instagram photos with these fields for each photo: 'image','link','thumbnail'
#     schools # list of schools
#     jobs # list of jobs
#
#     def get_photos(width=WIDTH) :
#         # a list of photo URLS with either of these widths ["84","172","320","640"] {
