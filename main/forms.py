from django import forms

class CreateList(forms.Form):
    name = forms.CharField(label="Name", max_length=100, required=False)
    check = forms.BooleanField()

