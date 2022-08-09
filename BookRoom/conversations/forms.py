from django import forms


class StartNewConversationFromProfile(forms.Form):
    subject = forms.CharField(label='', max_length=256, widget=forms.TextInput({'style': 'width: 35%;',
                                                                                "placeholder": "Conversation subject"}))

    message = forms.CharField(widget=forms.Textarea({'style': 'width: 70%; height: 200px',
                                                     }), label='')


class ReplyToConversation(forms.Form):
    message = forms.CharField(widget=forms.Textarea({'style': 'width: 60%; height: 150px'}), label='')
