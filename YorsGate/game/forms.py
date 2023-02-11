from django import forms


class CharForm(forms.Form):
    nickname = forms.CharField(max_length=14, min_length=3)


class MessageForm(forms.Form):
    message = forms.CharField(max_length=90)