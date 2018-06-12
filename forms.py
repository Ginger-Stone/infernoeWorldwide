from django import forms

class ContactForm(forms.Form):
    subject= forms.CharField(label='Your Name', max_length=100)
    your_email = forms.EmailField()
    phone_number = forms.CharField(label='eg. 0712345678', max_length=10)
    cc_myself = forms.BooleanField(required=False)
    message = forms.CharField(widget=forms.Textarea)

