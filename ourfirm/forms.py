from django import forms



class CallMeForm(forms.Form):
    contact_name = forms.CharField(required=True)
    contact_phone=forms.CharField(required=True)

    