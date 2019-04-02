from django.shortcuts import render, redirect

# Create your views here.
from .forms import ArtForm


def Art_create_view(request):

	form = ArtForm(request.POST or None)
	if request.method == 'POST':
		if 'logoutform' in request.POST:
			request.session['is_login'] = False
			return redirect('/login/') 

		if 'uploadform' in request.POST:
			if form.is_valid():
				form.save()
				form = ArtForm()

	context = {
		"form" : form	
	}

	return render(request, "art/art_create.html", context)