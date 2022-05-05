from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, Answer, Topic, Theme


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):

        model = CustomUser
        fields = ('username', 'email')


class CustomUserRegistrationForm(forms.ModelForm):

    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput)

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email')

        def clean_password2(self):
            cd = self.cleaned_data
            if cd['password'] != cd['password2']:
                raise forms.ValidationError('Passwords don\'t match.')
            return cd['password2']


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email')


class LoginForm(forms.Form):

    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class AnswerForm(forms.ModelForm):

    class Meta:
        model = Answer
        fields = ('answerText',)


class TopicForm(forms.ModelForm):

    class Meta:
        model = Topic
        fields = ('topicTitle', 'topicText')


class ThemeForm(forms.ModelForm):

    class Meta:
        model = Theme
        fields = ('themeTitle', 'themeText')





