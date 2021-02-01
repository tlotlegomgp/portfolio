from django import forms


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=35, widget=forms.TextInput(
        attrs={'class': "form-control", 'name': "subject", 'required': "", 'placeholder': "Subject", 'style': 'background-color: #2a2b2e;'}))
    email = forms.EmailField(max_length=50, widget=forms.EmailInput(attrs={
                             'class': "form-control", 'name': "email", 'required': "", 'placeholder': "Your Email", 'style': 'background-color: #2a2b2e;'}))
    message = forms.CharField(max_length=250, widget=forms.Textarea(
        attrs={'class': "form-control", 'name': "message", 'required': "", 'placeholder': "Message", 'style': 'background-color: #2a2b2e;'}))
