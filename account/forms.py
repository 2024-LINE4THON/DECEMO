from django import forms
from django.contrib.auth.models import User
import re

class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, min_length=8, label="password")
    password_confirm = forms.CharField(widget=forms.PasswordInput, label="password check")
    username = forms.CharField(
        max_length=20,
        required=True,
        label="id",
        help_text=""
    )

    class Meta:
        model = User
        fields = ['username', 'password']

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("중복되는 아이디입니다.")
        return username

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 8 or not re.search(r'\d', password) or not re.search(r'[a-zA-Z]', password):
            raise forms.ValidationError("영문/숫자 포함 8글자 이상 입력해주세요.")
        return password
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")

        if password and password_confirm and password != password_confirm:
            self.add_error("password_confirm", "비밀번호가 일치하지 않습니다.")

class LoginForm(forms.Form):
    username = forms.CharField(max_length=20, required=True, label="id")
    password = forms.CharField(widget=forms.PasswordInput, required=True, label="password")