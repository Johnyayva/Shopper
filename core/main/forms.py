from django import forms
from django.contrib.auth.forms import UserCreationForm
from users.models import CustomUser
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox


class NewUserForm(UserCreationForm):
	email = forms.EmailField(max_length=200, help_text='Required')
	captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox)
    
	class Meta:
		model = CustomUser
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user



	
