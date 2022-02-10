from django import forms
from . import models

class projectForm(forms.ModelForm):

	class Meta:
		model = models.Projects
		fields = ['projectName', 'projectDescription']
		labels = {'projectName': 'Project Name', 'projectDescription': 'Description'}

class mediaForm(forms.ModelForm):
	class Meta:
		model = models.Media
		fields = ['mediaType', 'mediaName', 'projectID', 'price']
		labels = {'mediaType': 'Media Type', 'mediaName': 'Media Name', 'projectID': 'Project', 'price': 'Print price'}