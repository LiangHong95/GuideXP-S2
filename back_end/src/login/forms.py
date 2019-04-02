from .models import AdminRegistration


from django import forms


class Login(forms.ModelForm):
	class Meta:
		model = AdminRegistration
		fields = [
			'user_name', 
			'user_pwd', 
			'user_email',
		]