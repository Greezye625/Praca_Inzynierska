from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from accounts.models import UserProfile
from django.forms import inlineformset_factory
from django import forms


class AvatarChangeForm(forms.Form):
    avatar = forms.CharField(label='new avatar', max_length=256)


class UserCreateForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Display Name'
        self.fields['email'].label = 'Email Address'

# class UserProfileForm(forms.ModelForm):
#
#     class Meta:
#         model = UserProfile
#         exclude = ()


# UserProfileFormSet = inlineformset_factory(get_user_model(), UserProfile, fields=('avatar',))


# class UserForm(forms.ModelForm):
#
#     class Meta:
#         model = get_user_model()
#         fields = ['username', 'email']
#
#     password1 = forms.CharField(widget=forms.PasswordInput, label='Password')
#     password2 = forms.CharField(widget=forms.PasswordInput, label='Confirm Password')
