from django import forms


class UploadFileForm(forms.Form):
    photo = forms.FileField()
