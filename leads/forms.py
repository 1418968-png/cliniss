from django import forms

from .models import Lead


class LeadForm(forms.ModelForm):
    next = forms.CharField(widget=forms.HiddenInput, required=False)

    class Meta:
        model = Lead
        fields = [
            'lead_type',
            'language',
            'name',
            'phone',
            'email',
            'message',
            'consent',
        ]
        widgets = {
            'lead_type': forms.Select(attrs={'class': 'form-control'}),
            'language': forms.HiddenInput(),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ваше имя / Your name'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+7 (___) ___-__-__'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'email@example.com'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Комментарий'}),
            'consent': forms.CheckboxInput(attrs={'class': 'form-check'}),
        }

    def clean_consent(self):
        consent = self.cleaned_data['consent']
        if not consent:
            raise forms.ValidationError('Необходимо согласие на обработку персональных данных.')
        return consent
