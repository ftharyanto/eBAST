from django import forms
from .models import ChecklistSeiscompModel, OperatorModel, StationListModel

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
            'tanggal': forms.TextInput(attrs={
                'class': 'datepicker',
                'name': 'tanggal',
                'placeholder': 'yyyy-mm-dd',

            })
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

class StationListForm(forms.ModelForm):
    # create meta class
    class Meta:
        # specify model to be used
        model = StationListModel

        # specify fields to be used
        fields = '__all__'
        widgets = {
            'kode': forms.TextInput(attrs={'placeholder': 'Kode Stasiun'}),
            'lokasi': forms.TextInput(attrs={'placeholder': 'Lokasi Stasiun'}),
            'tipe': forms.TextInput(attrs={'placeholder': 'Garansi atau Nongaransi'}),
        }
        labels = {
            'kode': ('Kode'),
            'stasiun': ('Lokasi Stasiun'),
            'tipe': ('Tipe Stasiun'),
        }
