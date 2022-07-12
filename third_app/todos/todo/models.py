from django.db import models
from django.contrib.auth.models import User

class Todo(models.Model):
    title=models.CharField(max_length=100)
    memo=models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    date_completed = models.DateTimeField(null=True, blank=True)
    important = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
# Create your models here.
#models.CASCADE - если пользователь удален, то удалятся все задачи
#models.PROTECTED - запрещает удалять пользователя, пока у него есть задачи.
#models.SET_NULL - задачи остануться при удалении пользователя, даже при удалении пользователя. Но значение в поле
# в поле выполнения задачи изменится на None
#models.SET_NULL - задачи остануться при удалении пользователя, даже при удалении пользователя. Но значение в поле
# в поле выполнения задачи изменится на по умолчанию