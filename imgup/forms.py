from django import forms

class ImgUploadForm(forms.Form):
	file  = forms.ImageField()