from django import forms


class StartNewConversationFromProfile(forms.Form):
    subject = forms.CharField(label='subject: ', max_length=256)

    message = forms.CharField(widget=forms.Textarea, label='')


class ReplyToConversation(forms.Form):
    message = forms.CharField(widget=forms.Textarea, label='')
