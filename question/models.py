from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):
    date = models.DateField(unique=True)  # 날짜마다 하나의 질문
    text = models.TextField()  # 질문 내용

    def __str__(self):
        return f"{self.date} - {self.text}"

class Answer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    response = models.TextField()  # 사용자의 답변
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.question.date}"
