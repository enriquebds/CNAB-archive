from django import forms

class UploadArchiveForm(forms.Form):
    file = forms.FileField()