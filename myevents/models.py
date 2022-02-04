from datetime import datetime
from django.db import models

BG_styles = [
    ('bg-primary text-white', 'primary'),
    ('bg-secondary text-white', 'secondary'),
    ('bg-success text-white', 'success'),
    ('bg-warning text-dark', 'warning'),
    ('bg-danger text-white', 'danger'),
    ('bg-info text-white', 'info'),
    ('bg-light text-dark', 'light'),
    ('bg-dark text-white', 'dark'),
]


class My_event(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    csstag = models.CharField(choices=BG_styles, max_length=50,default="primary")
    time = models.TimeField()


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Событие'
        verbose_name_plural = 'События'