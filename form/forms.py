from django import forms
from .models import Babiesform
from django.utils import timezone
class BabiesFormForm(forms.ModelForm):
    class Meta:
        model = Babiesform
        fields = '__all__'
        widgets = {
            'name_of_the_baby': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.TextInput(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'parents_name': forms.TextInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'babys_number': forms.TextInput(attrs={'class': 'form-control'}),
            'comment': forms.Textarea(attrs={'class': 'form-control'}),
            'timein': forms.TimeInput(attrs={'class': 'form-control'}),
            'timeout': forms.TimeInput(attrs={'class': 'form-control'}),
            'c_stay': forms.Select(attrs={'class': 'form-control'}),
            'c_fees': forms.Select(attrs={'class': 'form-control'}),
            'name_of_the_person_brought_by_the_baby': forms.TextInput(attrs={'class': 'form-control'}),}

