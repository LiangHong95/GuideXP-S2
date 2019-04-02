from django import forms


from .models import ArtData


class ArtForm(forms.ModelForm):
	class Meta:
		model  = ArtData
		fields = [
			'art_author',
			'art_name',
			'art_description',
			'art_img'
		]