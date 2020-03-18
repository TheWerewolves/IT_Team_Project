from django import forms
from django.contrib.auth.models import User

from gamers_havn.models import Account


# class ArticleForm(forms.ModelForm):
#     title = forms.CharField(max_length=Page.TITLE_MAX_LENGTH,
#                            help_text="Please enter the title of the page.")
#     url = forms.URLField(max_length=Page.URL_MAX_LENGTH,
#                            help_text="Please enter the URL of the page.")
#     views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

#     class Meta:
#         model = Page
#         exclude = ('category', )

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'email', 'password',)

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ('age', 'portrait',)
    