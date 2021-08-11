from django import forms


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=35, widget=forms.TextInput(
        attrs={'class': "form-control", 'name': "subject", 'placeholder': "Subject", 'style': 'background-color: rgb(52,58,64); color: white;'}), required=True)
    email = forms.EmailField(max_length=50, widget=forms.EmailInput(attrs={
                             'class': "form-control", 'name': "email", 'placeholder': "Your Email", 'style': 'background-color: rgb(52,58,64); color: white;'}), required=True)
    message = forms.CharField(max_length=600, widget=forms.Textarea(
        attrs={'class': "form-control", 'name': "message", 'placeholder': "Message", 'style': 'background-color: rgb(52,58,64); color: white;'}), required=True)
