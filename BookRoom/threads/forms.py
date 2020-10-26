from django import forms


class AddComment(forms.Form):
    text_content = forms.CharField(widget=forms.Textarea, label='')
