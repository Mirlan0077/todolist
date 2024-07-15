from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

STATUS_CHOICES = [
    ('todo', 'To Do'),
    ('in_progress', 'In Progress'),
    ('done', 'Done'),
]

TYPE_CHOICES = [
    ('bug', 'Bug'),
    ('feature', 'Feature'),
]


def validate_no_special_characters(value):
    if not value.isalnum():
        raise ValidationError(_('Поле должно быть буквенно-цифровым'), params={'value': value})


def validate_description_length(value):
    if len(value) < 10:
        raise ValidationError(_('Длина описания должна составлять не менее 10 символов'))


class Task(models.Model):
    objects = None
    title = models.CharField(max_length=255)
    description = models.TextField(validators=[validate_description_length])
    completed = models.BooleanField(default=False)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='todo')
    task_type = models.CharField(max_length=20, choices=TYPE_CHOICES, default='feature')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
