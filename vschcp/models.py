"""
For Models
"""
from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import now as djtnow


class Article(models.Model):
    """
    Model for managing author publications
    """
    title = models.CharField(
        verbose_name='Title',
        blank=False,
        default='Sample Article',
        max_length=30,
        unique=True
    )
    author = models.OneToOneField(
        to=User,
        verbose_name='Author',
        on_delete=models.CASCADE
    )
    summary = models.CharField(
        verbose_name='Summary',
        default='Sample summary',
        max_length=140
    )
    article = models.TextField(
        verbose_name='Article',
        blank=False,
        default='Here is the sample article',
        max_length=10000
    )
    date = models.DateField(
        verbose_name='Date',
        blank=False,
        default=djtnow,

    )

    def __str__(self) -> str:
        return f'{self.title} by {self.author.username}; {self.date}'
