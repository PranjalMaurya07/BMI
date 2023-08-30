from django.forms import ModelForm
from myapp.models import *

class createform(ModelForm):
    
    class Meta:
        model=bmi
        fields=['weight','height']