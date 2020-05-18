from .models import Resume
from django import forms


# Model based form
class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ['firstname', 'lastname', 'email', 'phone']
        labels = {
            'firstname': 'First Name',
            'lastname': 'Last Name',
            'email': 'Email ID',
            'phone': 'Phone Number',
        }
