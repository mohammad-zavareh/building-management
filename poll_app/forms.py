from django import forms


class CreatePollForm(forms.Form):
    question = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'سوال'}))
    option_1 = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'گزینه 1'}))
    option_2 = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'گزینه 2'}))
    option_3 = forms.CharField(required=False, widget=forms.HiddenInput(attrs={'placeholder': 'گزینه 3'}))
    option_4 = forms.CharField(required=False, widget=forms.HiddenInput(attrs={'placeholder': 'گزینه 4'}))
    option_5 = forms.CharField(required=False, widget=forms.HiddenInput(attrs={'placeholder': 'گزینه 5'}))
    option_6 = forms.CharField(required=False, widget=forms.HiddenInput(attrs={'placeholder': 'گزینه 6'}))