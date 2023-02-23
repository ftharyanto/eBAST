from django import forms
from .models import ChecklistSeiscompModel
 
 
# creating a form
class ChecklistSeiscompForm(forms.ModelForm):
 
    # create meta class
    class Meta:
        # specify model to be used
        model = ChecklistSeiscompModel
 
        # specify fields to be used
        fields = [
            'date',
            'gaps',
            'spikes',
            'blanks',
            'operator',
            'group',
            'gaps',
            'gaps',
        ]
        widgets = {
            'date': forms.TextInput(attrs={'class': 'input_date'}),
        }