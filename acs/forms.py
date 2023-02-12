from django import forms
from acs.models import Enquiry
class EnquiryForm(forms.ModelForm):
    class Meta:
        model=Enquiry
        fields="__all__"