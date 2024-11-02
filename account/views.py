from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User
from .forms import SignUpForm, LoginForm
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def check_username(request):
    username = request.GET.get('username', None)
    data = {
        'is_taken': User.objects.filter(username=username).exists()
    }
    return JsonResponse(data)

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('home')
            else:
                form.add_error(None, "아이디 또는 비밀번호가 올바르지 않습니다.")
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def logout(request):
    auth_logout(request)
    return redirect('index')

def index(request):
    return render(request, 'index.html')

def test(request):
    return render(request, 'test.html')

@login_required
def home(request):
    # BGM 상태를 세션에서 읽어오기
    is_playing = request.session.get('bgm_playing', True)  # 기본값을 True로 설정
    return render(request, 'home.html', {'isPlaying': is_playing})

@login_required
def toggle_bgm(request):
    # BGM 상태 토글
    current_state = request.session.get('bgm_playing', True)
    request.session['bgm_playing'] = not current_state  # 현재 상태 반전
    return redirect('home')  # 홈으로 리다이렉트