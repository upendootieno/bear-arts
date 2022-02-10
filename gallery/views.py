from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Projects, Media, MediaTypes
from django.db.models import F
from . import forms
from django.contrib import messages

#for uploading images to sirv
from SirvPy import upload_files, get_access

def index(request):
	images = Projects.objects.all().order_by("-creationDate")[:5]
	all_images = Projects.objects.all().order_by("-creationDate")

	context = {
	'images': images,
	'all_images': all_images,
	}

	return render(request, 'gallery/index.html', context)

def projectPage(request, projectID = None):
	images = Media.objects.filter(projectID__projectID = projectID)
	projectDetails = Projects.objects.get(projectID = projectID)

	context = {
		'projectDetails':projectDetails,
		'images': images,
	}

	return render(request, 'gallery/projectPage.html', context)

def uploadFile(projectName, file):
	clientId = 'xxx'
	clientSecret = 'xxx'

	upload_to = '/BearArts/%s/%s' %(projectName, file)
	access_token = get_access(clientId, clientSecret)['token']

	confirm_upload = upload_files(access_token, file, upload_to)
	fileUrl = 'sirv-url.com' %upload_to

	if confirm_upload.status_code == 200:
		return fileUrl
	else:
		return 'upload_failed'

def dashboard(request):
	projectForm = forms.projectForm()
	mediaForm = forms.mediaForm()
	context = {
	'projectForm': projectForm,
	'mediaForm': mediaForm,
	}

	if request.method == 'POST' and 'create_project' in request.POST:
		projectForm = forms.projectForm(request.POST)

		if projectForm.is_valid():
			projectInstance = projectForm.save(commit = False)
			file = request.FILES['projectThumbnailFile']
			thumbnail = uploadFile(request.POST.get('projectName'), file)
			default_thumbnail = 'sirv-url.com/image.jpg'

			if thumbnail == 'upload_failed':
				projectInstance.projectThumbnail = default_thumbnail
				messages.warning(request, 'Thumbnail upload failed.')
			else:
				projectInstance.projectThumbnail = thumbnail
				messages.success(request, 'Thumbnail uploaded.')

				#create Media instance for the thumnail
				media = Media(mediaType = MediaTypes.objects.get(mediaTypeID = 'photograph'), mediaName = file, mediaUrl = thumbnail, projectID = projectInstance)

			projectInstance.save()
			media.save()
			messages.success(request, 'Project created')
			return HttpResponseRedirect('dashboard')
		else:
			messages.warning(request, 'Something went wrong')
			return HttpResponseRedirect('dashboard')

	if request.method == 'POST' and 'create_media' in request.POST:
		mediaForm = forms.mediaForm(request.POST)

		if mediaForm.is_valid():
			mediaInstance = mediaForm.save(commit = False)
			file = request.FILES['mediaFile']
			project = Projects.objects.get(projectID = request.POST.get('projectID'))
			uploadMedia = uploadFile(project.projectName, file )

			mediaInstance.mediaUrl = uploadMedia

			mediaInstance.save()
			return HttpResponseRedirect('dashboard')

	return render(request, 'gallery/dashboard.html', context)