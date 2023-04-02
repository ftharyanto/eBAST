from django import forms
from .models import ChecklistSeiscompModel, OperatorModel


# creating a form
class InputForm(forms.ModelForm):
    operator = forms.ModelChoiceField(
        queryset=OperatorModel.objects.all(), initial=0)

    # create meta class
    class Meta:
        # specify model to be used
        model = ChecklistSeiscompModel

        # specify fields to be used
        fields = '__all__'

        widgets = {
            'gaps': forms.TextInput(attrs={
                'class': 'tooltipped',
                'data-position': 'bottom',
                'data-tooltip': 'shift+scroll untuk scrolling secara horizontal',
                'placeholder': 'ABCD EFGH IJKL MNOP QRST UVWX YZZZ',
            }),
            'spikes': forms.TextInput(attrs={
                'class': 'tooltipped',
                'data-position': 'bottom',
                'data-tooltip': 'shift+scroll untuk scrolling secara horizontal',
                'placeholder': 'ABCD EFGH IJKL MNOP QRST UVWX YZZZ',
            }),
            'blanks': forms.TextInput(attrs={
                'class': 'tooltipped',
                'data-position': 'bottom',
                'data-tooltip': 'shift+scroll untuk scrolling secara horizontal',
                'placeholder': 'ABCD EFGH IJKL MNOP QRST UVWX YZZZ',
            }),
            'slmon': forms.NumberInput(attrs={
                'class': 'tooltipped',
                'data-position': 'bottom',
                'data-tooltip': 'shift+scroll untuk scrolling secara horizontal',
                'placeholder': 'Jumlah sensor yang delay lebih dari 30 menit. Contoh: 30',
            }),
            'tanggal': forms.DateInput(),
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
