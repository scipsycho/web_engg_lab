from django import forms

class rsaInput(forms.Form):

    user_name = forms.CharField(label='Name', max_length=100)
    user_email = forms.EmailField(label='Email', max_length=100)
    user_message = forms.CharField(label='Message', widget=forms.Textarea, max_length=1000)


class desInput(forms.Form):

    key = forms.CharField(label="Key", max_length=16)
    message = forms.CharField(label='Message', widget=forms.Textarea, max_length=1000)
