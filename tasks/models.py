from django.db import models

class Task(models.Model):
    STATUS_CHOICES = [
        ('new', 'Новая'),
        ('in_progress', 'В процессе'),
        ('done', 'Сделано'),
    ]

    description = models.CharField(max_length=255)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')
    due_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.description



    from django.db import models

    class Task(models.Model):
        title = models.CharField(max_length=200)
        completed = models.BooleanField(default=False)
        description = models.TextField(blank=True)  # новое поле для подробного описания

        def __str__(self):
            return self.title
