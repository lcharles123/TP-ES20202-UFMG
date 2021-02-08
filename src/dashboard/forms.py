from django import forms

class AcoesForm(forms.Form):
   acao = forms.CharField(widget=forms.Select)