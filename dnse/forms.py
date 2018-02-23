from django import forms

class SearchForm(forms.Form):
    search_query = forms.CharField(label="", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'width:70%;'}),)
