from django import forms

from .models import Kontakt


class ContactForm(forms.ModelForm):
    imie = forms.CharField(
        label='Imię',
        widget=forms.TextInput(
            attrs={
                "class": "u-border-1 u-border-black u-input u-input-rectangle u-white u-input-1",
            }
        )
    )

    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(
            attrs={
                "class": "u-border-1 u-border-black u-input u-input-rectangle u-white u-input-2",
            }
        )
    )

    tresc = forms.CharField(
        label='Wiadomości',
        widget=forms.Textarea(
            attrs={
                "class": "u-border-1 u-border-black u-input u-input-rectangle u-white u-input-3",
                "rows": '4',
                "cols": '50'
            }
        )
    )

    class Meta:
        model = Kontakt
        fields = '__all__'
