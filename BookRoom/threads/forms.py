from django import forms


class AddComment(forms.Form):
    text_content = forms.CharField(widget=forms.Textarea, label='')


class AddThread(forms.Form):
    name = forms.CharField(max_length=256)

    first_comment = forms.CharField(widget=forms.Textarea, label='')
