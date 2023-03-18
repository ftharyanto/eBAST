from django import forms
from .models import ChecklistSeiscompModel, OperatorModel


# creating a form
class InputForm(forms.ModelForm):
    operator = forms.ModelChoiceField(queryset=OperatorModel.objects.all(), initial=0)

    # create meta class
    class Meta:
        # specify model to be used
        model = ChecklistSeiscompModel

        # specify fields to be used
        fields = '__all__'

        widgets = {
            'gaps': forms.TextInput(attrs={'placeholder': 'ABCD EFGH'}),
            'spikes': forms.TextInput(attrs={'placeholder': 'ABCD EFGH'}),
            'blanks': forms.TextInput(attrs={'placeholder': 'ABCD EFGH'}),
            'tanggal': forms.TextInput(attrs={'class': 'datepicker', 'placeholder': 'Masukkan Tanggal'}),
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
