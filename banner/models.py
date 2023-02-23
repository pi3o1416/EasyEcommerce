
from django.utils.translation import gettext_lazy as _
from django.db import models


class Banner(models.Model):
    headline = models.CharField(
        verbose_name=_("Banner Headline"),
        max_length=500
    )
    image = models.ImageField(
        verbose_name=("Banner Image")
    )
    top_text = models.CharField(
        verbose_name=_("Top text"),
        max_length=500,
    )
    bottom_text = models.CharField(
        verbose_name=_("Bottom text"),
        max_length=500,
    )
    optional_text = models.CharField(
        verbose_name=_("Optional text"),
        max_length=500,
    )

