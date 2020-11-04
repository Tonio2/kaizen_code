from django.db import models

class Todo(models.Model):
    todo_title = models.CharField(max_length = 200)
    done = models.BooleanField(default = False)

    def __str__(self):
        return self.todo_title
