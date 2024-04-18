from django import forms
from .models import Babiesform
from django.utils import timezone
class BabiesFormForm(forms.ModelForm):
    class Meta:
        model = Babiesform
        fields = '__all__'

# widget = {
#     "name":forms.TextInput(attrs={'class': 'form-control'})
# }        