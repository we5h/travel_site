from bootstrap_modal_forms.forms import BSModalModelForm
from django import forms

from .models import BuyTour


class BuyTourForm(BSModalModelForm):
    """Форма покупки тура"""
    class Meta:
        model = BuyTour
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'tour': forms.Select(attrs={'class': 'form-control'})
        }
