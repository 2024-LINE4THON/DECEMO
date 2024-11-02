from django.contrib import admin
from .models import Question, Answer

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('date', 'text')  # 관리 페이지에서 보이는 필드
    search_fields = ('text',)        # 텍스트로 검색 가능하게 설정

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('user', 'question', 'response', 'created_at')  # Answer 모델의 필드 표시
    list_filter = ('user', 'question__date')  # 필터로 사용자와 질문 날짜 추가
    search_fields = ('response',)  # 답변 내용 검색 가능하게 설정