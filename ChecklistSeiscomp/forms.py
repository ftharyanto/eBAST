from django import forms
from .models import ChecklistSeiscompModel, OperatorModel
 
 
# creating a form
class InputForm(forms.ModelForm):
 
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
        ]
        widgets = {
            'date': forms.TextInput(attrs={'class': 'input_date'}),
            'group': forms.TextInput(attrs={'class': 'group'}),
            
        }
        labels = {
            'group': ('Kelompok'),
            'date': ('Tanggal')
        }

class OperatorForm(forms.ModelForm):
    # create meta class
    class Meta:
        # specify model to be used
        model = OperatorModel
 
        # specify fields to be used
        fields = [
            'name',
        ]
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Nama'}),
        }
        labels = {
            'name': ('Nama'),
        }