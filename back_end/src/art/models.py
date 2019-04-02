from django.db import models

# Create your models here.
class ArtData(models.Model):
	art_author       = models.CharField(max_length=128, blank=True, null=True)  #foreign key
	art_name  		 = models.CharField(max_length=128, blank=True, null=True)
	#art_gallery      = models.CharField(max_length=128, blank=True, null=True) foreign key
	art_description  = models.CharField(max_length=256, blank=True, null=True)
	art_img          = models.ImageField(upload_to='imgs/',blank=True, null=True)


# class ArtGallery(models.Model):
# 	art_gallery 


# class ArtAuthor(models.Model):
