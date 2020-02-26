from django.db import models

from django.conf import settings
from django.contrib.auth.models import User

from django.utils.translation import gettext_lazy as _

import os

__all__ = [ "Blog" ]

class BlogManager(models.Manager):
    """Model Manager for Profile model"""
    def get_queryset(self):
        return super(BlogManager, self).get_queryset().filter(published=True)

class Blog(models.Model):

    author = models.ForeignKey(
        to=User, 
        verbose_name=_("Author"),
        on_delete=models.CASCADE
    )

    title = models.CharField(verbose_name=_("Title"), max_length=60)
    subject = models.CharField(verbose_name=_("Subject"), max_length=100)
    body = models.CharField(verbose_name=_("Body"), max_length=1500)
    published = models.BooleanField(verbose_name=_("Published"), default=False)

    objects = models.Manager()
    blogs = BlogManager()

    def __str__(self):
        return "%s"% self.author.username
