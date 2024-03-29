from django import forms


class CreatePollForm(forms.Form):
    question = forms.CharField(required=True, widget=forms.Textarea(
        attrs={'placeholder': 'سوال', 'class': 'textinput textInput form-control'}))
    option_1 = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'placeholder': 'گزینه 1', 'class': 'textinput textInput form-control'}))
    option_2 = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'placeholder': 'گزینه 2', 'class': 'textinput textInput form-control'}))
    # option_3 = forms.CharField(required=False, widget=forms.HiddenInput(
    #     attrs={'placeholder': 'گزینه 3', 'class': 'textinput textInput form-control'}))
    # option_4 = forms.CharField(required=False, widget=forms.HiddenInput(
    #     attrs={'placeholder': 'گزینه 4', 'class': 'textinput textInput form-control'}))
    # option_5 = forms.CharField(required=False, widget=forms.HiddenInput(
    #     attrs={'placeholder': 'گزینه 5', 'class': 'textinput textInput form-control'}))
    # option_6 = forms.CharField(required=False, widget=forms.HiddenInput(
    #     attrs={'placeholder': 'گزینه 6', 'class': 'textinput textInput form-control'}))
