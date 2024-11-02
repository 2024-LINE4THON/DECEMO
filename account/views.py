from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User
from .forms import SignUpForm, LoginForm
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from datetime import datetime
from question.models import Answer

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

@login_required
def home(request):
    # 임의로 현재 날짜를 2024년 12월 3일로 설정
    today = datetime(2024, 12, 3)
    target_date = datetime(2025, 1, 1)
    d_day = (target_date - today).days  # 남은 일수 계산
    
    is_playing = request.session.get('bgm_playing', True)  # 기본값 True로 설정

    # 사용자가 작성한 답변 개수
    total_questions = 31
    answered_count = Answer.objects.filter(user=request.user, question__date__month=12).count()
    progress_percentage = (answered_count / total_questions) * 100

    return render(request, 'home.html', {
        'isPlaying': is_playing,
        'today': today,
        'd_day': d_day,
        'answered_count': answered_count,
        'total_questions': total_questions,
        'progress_percentage': progress_percentage,
        'username': request.user.username  # 사용자 이름 전달
    })

@login_required
def toggle_bgm(request):
    current_state = request.session.get('bgm_playing', True)
    request.session['bgm_playing'] = not current_state 
    return redirect('home')