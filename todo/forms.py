from django import forms
from . import models

class TodoForm(forms.Form):
    task = forms.CharField(max_length=255)
    due = forms.DateTimeField(
        widget=forms.DateTimeInput(format="%Y/%m/%d")
        )

    def save(self):
        new_task = self.cleaned_data["task"]
        its_due = self.cleaned_data["due"]
        if models.Todo.objects.filter(task=new_task).count() == 0:
            todo = models.Todo(task=new_task, due=its_due, done=False);
            todo.save()
