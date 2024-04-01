from django import forms


class CreatePollForm(forms.Form):
    question = forms.CharField(required=True, widget=forms.Textarea(
        attrs={'placeholder': 'سوال', 'class': 'textinput textInput form-control'}))
    option_1 = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'placeholder': 'گزینه 1', 'class': 'textinput textInput form-control'}))
    option_2 = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'placeholder': 'گزینه 2', 'class': 'textinput textInput form-control'}))