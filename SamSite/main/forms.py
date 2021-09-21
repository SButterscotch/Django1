from django import forms

class CreateForm(forms.Form):
    name = forms.CharField(label="Name", max_length=200, required=False)
    check = forms.BooleanField(required=False)
    captcha = forms.IntegerField(label= '2 + 2', label_suffix=' =')

