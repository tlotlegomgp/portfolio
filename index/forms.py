from django import forms


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=35, widget=forms.TextInput(
        attrs={'class': "form-control", 'name': "subject", 'required': "", 'placeholder': "Subject", 'style': 'background-color: rgb(52,58,64); color: white;'}))
    email = forms.EmailField(max_length=50, widget=forms.EmailInput(attrs={
                             'class': "form-control", 'name': "email", 'required': "", 'placeholder': "Your Email", 'style': 'background-color: rgb(52,58,64); color: white;'}))
    message = forms.CharField(max_length=250, widget=forms.Textarea(
        attrs={'class': "form-control", 'name': "message", 'required': "", 'placeholder': "Message", 'style': 'background-color: rgb(52,58,64); color: white;'}))
