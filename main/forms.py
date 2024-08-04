from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import ScreenTime, CustomUser


class ScreenTimeForm(forms.ModelForm):
    hours = forms.IntegerField(min_value=0, required=True, label='Hours',
        widget=forms.NumberInput(attrs={
            'class': 'screen-time-input',  # 여기에 원하는 CSS 클래스를 지정
        }))
    minutes = forms.IntegerField(min_value=0, max_value=59, required=True, label='Minutes',
        widget=forms.NumberInput(attrs={
            'class': 'screen-time-input',  # 여기에 원하는 CSS 클래스를 지정
        }))

    class Meta:
        model = ScreenTime
        fields = []

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance:
            self.fields['hours'].initial = self.instance.total_minutes // 60
            self.fields['minutes'].initial = self.instance.total_minutes % 60

    def save(self, commit=True):
        self.instance.total_minutes = self.cleaned_data['hours'] * 60 + self.cleaned_data['minutes']
        return super().save(commit)

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
        label="아이디",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    email = forms.EmailField(
        label="이메일",
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    password1 = forms.CharField(
        label="비밀번호",
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    password2 = forms.CharField(
        label="비밀번호 재확인",
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2')