from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Question, Answer
from .forms import AnswerForm

@login_required
def calendar_view(request):
    days = list(range(1, 32))  # 1일부터 31일까지의 숫자 리스트
    rows = [days[i:i + 5] for i in range(0, len(days), 5)]  # 5개씩 나누어 리스트 생성

    # 사용자가 이미 답변을 작성한 날짜 가져오기 (12월에 한정)
    answered_days = Answer.objects.filter(user=request.user, question__date__month=12).values_list('question__date__day', flat=True)

    return render(request, 'calendar.html', {
        'rows': rows,
        'answered_days': list(answered_days)  # 답변이 작성된 날짜 리스트
    })

@login_required
def question_detail(request, day):
    question = get_object_or_404(Question, date__day=day, date__month=12)
    
    # 현재 사용자가 이 질문에 대한 답변을 이미 작성했는지 확인
    answer_exists = Answer.objects.filter(user=request.user, question=question).exists()

    # 이미 답변이 존재하는 경우 메시지를 표시하고 폼을 숨김
    if answer_exists:
        return render(request, 'question_detail.html', {
            'question': question,
            'message': "해당 날짜는 이미 답변을 작성했습니다."
        })

    # 답변이 없는 경우, 폼을 보여줌
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            new_answer = form.save(commit=False)
            new_answer.user = request.user
            new_answer.question = question
            new_answer.save()
            return redirect('calendar')
    else:
        form = AnswerForm()

    return render(request, 'question_detail.html', {
        'question': question,
        'form': form
    })
