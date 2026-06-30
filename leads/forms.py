import re

from django import forms

from .models import Lead


class LeadForm(forms.ModelForm):
    next = forms.CharField(widget=forms.HiddenInput, required=False)
    website = forms.CharField(required=False, widget=forms.HiddenInput)

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

    def clean_website(self):
        if self.cleaned_data.get('website'):
            raise forms.ValidationError('Заявка отклонена.')
        return ''

    def clean_name(self):
        name = ' '.join(self.cleaned_data['name'].split())
        if len(name) < 2:
            raise forms.ValidationError('Укажите имя.')
        if re.search(r'https?://|www\.', name, flags=re.IGNORECASE):
            raise forms.ValidationError('Имя не должно содержать ссылку.')
        return name

    def clean_phone(self):
        phone = ' '.join(self.cleaned_data['phone'].split())
        digits = re.sub(r'\D', '', phone)
        if len(digits) < 6 or len(digits) > 15:
            raise forms.ValidationError('Укажите корректный номер телефона.')
        if len(phone) > 40:
            raise forms.ValidationError('Номер телефона слишком длинный.')
        return phone

    def clean_email(self):
        return self.cleaned_data.get('email', '').strip().lower()

    def clean_message(self):
        message = self.cleaned_data.get('message', '').strip()
        if len(message) > 2000:
            raise forms.ValidationError('Комментарий не должен превышать 2000 символов.')
        return message
