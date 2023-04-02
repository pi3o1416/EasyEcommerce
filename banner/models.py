
from django.db.models import UniqueConstraint, Q
from django.utils.translation import gettext_lazy as _
from django.db import models


class BannerQuerySet(models.QuerySet):
    def get_banners(self, banner_type):
        return self.filter(banner_type=banner_type)

    def count_active_banner(self, banner_type=None):
        if banner_type:
            self = self.get_banners(banner_type=banner_type)
        return self.count()


class Banner(models.Model):
    # TODO: Add image upload url
    class BannerPosition(models.TextChoices):
        TOP_BANNER = "TOP_BANNER", _("Top Banner")
        MIDDLE_LEFT = "MIDDLE_LEFT", _("Middle Left Banner")
        MIDDLE_RIGHT = "MIDDLE_RIGHT", _("Middle Right Banner")
        BOTTOM_BANNER = "BOTTOM_BANNER", _("Bottom Banner")

    headline = models.CharField(
        verbose_name=_("Banner Headline"),
        max_length=500
    )
    image = models.ImageField(
        verbose_name=("Banner Image"),
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
    redirect_url = models.URLField(
        verbose_name=_("Redirected URL"),
        null=True,
        blank=True,
    )
    banner_type = models.CharField(
        verbose_name=_("Banner Type"),
        max_length=50,
        choices=BannerPosition.choices,
        default=BannerPosition.TOP_BANNER
    )
    is_active = models.BooleanField(
        default=False,
        verbose_name=_("Is Active")
    )
    created_at = models.DateTimeField(
        verbose_name=_("Created at"),
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        verbose_name=_("Last updated at"),
        null=True,
        blank=True
    )
    objects = BannerQuerySet.as_manager()

    class Meta:
        constraints = [
            UniqueConstraint(
                name='unique_active_banner',
                fields=['banner_type', 'is_active'],
                condition=Q(banner_type__in=[
                    'MIDDLE_LEFT', 'MIDDLE_RIGHT', 'BOTTOM_BANNER']) & Q(is_active=True)
            )
        ]
