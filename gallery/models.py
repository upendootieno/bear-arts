from django.db import models

#to record project date
from django.utils import timezone

class Projects(models.Model):
	projectID = models.AutoField(primary_key = True)
	projectName = models.CharField(max_length = 50)
	creationDate = models.DateTimeField(default = timezone.now)
	projectThumbnail = models.URLField(max_length = 200)
	projectDescription = models.TextField(max_length = 1000)

	def __str__(self):
		return self.projectName

class MediaTypes(models.Model):
	mediaTypeID = models.CharField(primary_key = True, max_length = 15)

	def __str__(self):
		return self.mediaTypeID

class Media(models.Model):
	mediaID = models.AutoField(primary_key = True)
	mediaType = models.ForeignKey(MediaTypes, on_delete = models.CASCADE)
	mediaUrl = models.URLField(max_length = 200)
	mediaName = models.CharField(max_length = 20)
	projectID = models.ForeignKey(Projects, on_delete = models.CASCADE)
	price = models.IntegerField(default = 0)
	uploadDate = models.DateTimeField(default = timezone.now)

	def __str__(self):
		return self.mediaName