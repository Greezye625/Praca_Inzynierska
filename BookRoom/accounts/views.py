from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from accounts import forms
from accounts.models import UserProfile
from django.contrib.auth.models import User
# from extra_views import CreateWithInlinesView, InlineFormSetFactory
from django.views.generic import (CreateView, UpdateView,
                                  DeleteView, DetailView,
                                  ListView, )


def change_avatar(request):
    if request.method == 'POST':
        # form = forms.AvatarChangeForm(request.POST)
        form = forms.AvatarChangeForm(request.POST, request.FILES)

        if form.is_valid():
            user = request.user
            if hasattr(user, 'userprofile'):
                user.userprofile.avatar = form.files['avatar']
            else:
                user.userprofile = UserProfile(avatar=form.files['avatar'])
            user.userprofile.save()

        return redirect('accounts:user_profile_page', pk=request.user.pk)

    elif request.method == 'GET':
        form = forms.AvatarChangeForm()
        return render(request, 'accounts/change_avatar.html', context={'form': form})


def user_profile_page(request, pk):
    if request.method == 'POST':
        pass
    elif request.method == 'GET':
        profile_page_user = User.objects.get(pk=int(pk))
        return render(request, 'accounts/profile_page.html', context={'profile_page_user': profile_page_user})


# ----------------------------------------------------------------------------------


class CreateUserForm(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('accounts:login')

    template_name = 'accounts/signup.html'

    def form_valid(self, form):
        super(CreateUserForm, self).form_valid(form)

        user = self.object

        userprofile = UserProfile(user=user)

        userprofile.save()

        return HttpResponseRedirect(self.success_url)


# class UserInline(InlineFormSetFactory):
#     model = User
#     fields = ['username', 'email', 'password1', 'password2']


# class UserProfileInline(InlineFormSetFactory):
#     model = UserProfile
#     fields = ['avatar']
#     factory_kwargs = {'can_delete': False}
#
#
# class CreateUserProfileView(CreateWithInlinesView):
#     form_class = forms.UserForm
#     inlines = [UserProfileInline]
#     # fields = ['username', 'email', 'password']
#     template_name = 'accounts/signup.html'
#
#
#     def get_success_url(self):
#         return self.inlines[0].model.get_absolute_url(UserProfile)
#
#     def form_valid(self, form, inlines):
#         password1 = form.cleaned_data['password1']
#         password2 = form.cleaned_data['password2']
#
#         if password2 and password1:
#             if password1 != password2:
#                 # raise a ValidationError message
#                 pass
#
#             user = self.request.user  # at this point password is 'old_passord'
#             user.set_password(password1)  # now is 'password1'
#             user.save()  # 'password1' is correctly saved in db
#
#         return super(AdminProfile, self).forms_valid(form, inlines)


# class SignUp(CreateView):
#     model = UserProfile
#     fields = ['username', 'email', 'password1', 'password2']
#     # success_url = reverse_lazy('accounts:login')
#
#     template_name = 'accounts/signup.html'
