from django import forms


class AddComment(forms.Form):
    text_content = forms.CharField(widget=forms.Textarea(attrs={'style': 'width: 100%; height: 200px',
                                                                'placeholder': 'Add new comment'}), label='')


class AddThread(forms.Form):
    name = forms.CharField(max_length=256, label='', widget=forms.TextInput({"placeholder": "Title"}))

    first_comment = forms.CharField(widget=forms.Textarea, label='')
