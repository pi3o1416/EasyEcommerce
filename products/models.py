from django.core.validators import RegexValidator
from django.db.models import CheckConstraint, Q
from django.db import models
from django.utils.translation import gettext_lazy as _


class ProductColor(models.Model):
    color_name = models.CharField(
        verbose_name=_("Color Name"),
        max_length=50,
        validators=[
            RegexValidator(
                regex=r'^[A-Z]+$',
                message="Color name should be in capital letter"
            )
        ]
    )
    color_code = models.CharField(
        verbose_name=_("Color Code"),
        max_length=6,
        validators=[RegexValidator(
            regex=r'^#([a-fA-F0-9]{6}|[a-fA-F0-9]{3})$',
            message="Inavlid Color Code"
        )]
    )

    def __str__(self):
        return self.color_name


class ProductCategory(models.Model):
    category_name = models.CharField(
        verbose_name=_("Category Name"),
        max_length=200,
        unique=True,
        validators=[
            RegexValidator(
                regex=r'^[A-Z]{1}[a-z]*$',
                message="First Letter should be in capital followed by small case letter"
            )
        ]
    )

    def __str__(self):
        return self.category_name


class ProductTag(models.Model):
    tag_name = models.CharField(
        verbose_name=_("Tag Name"),
        max_length=200,
        unique=True,
        validators=[
            RegexValidator(
                regex=r'^[A-Z]{1}[a-z]*$',
                message='First letter should be in capital followed by small case latter'
            )
        ]
    )

    def __str__(self):
        return self.tag_name


class ProductDiscount(models.Model):
    discount_percent = models.IntegerField(
        verbose_name=_("Discount Percentage")
    )

    class Meta:
        constraints = [
            CheckConstraint(
                name='valid_discount_range',
                check=Q(discount_percent__gte=1) & Q(discount_percent__lte=99)
            )
        ]

    def __str__(self):
        return f'{self.discount_percent}% Discount'


class ProductBrand(models.Model):
    brand_name = models.CharField(
        verbose_name=_("Brand Name"),
        max_length=200,
        validators=[
            RegexValidator(
                regex=r'^[A-Z]{1}[a-z]*$',
                message="First Letter should be in capital followed by small case letter"
            )
        ]
    )

    def __str__(self):
        return self.brand_name


class Product(models.Model):
    name = models.CharField(
        verbose_name=_("Product Name"),
        max_length=500
    )
    slug = models.SlugField(
        verbose_name=_("Product Slug"),
        max_length=500
    )
    short_discription = models.TextField(
        verbose_name=_("Product Short Description")
    )
    description = models.TextField(
        verbose_name=_("Product Description")
    )
    price = models.DecimalField(
        verbose_name=_("Product Price"),
        max_digits=10,
        decimal_places=2
    )
    in_stock = models.BooleanField(
        verbose_name=_("Product In Stock"),
        default=False
    )
    product_brand = models.OneToOneField(
        to=ProductBrand,
        on_delete=models.RESTRICT,
        related_name='brand_products',
        verbose_name=_("Product Brand"),
        null=True,
        blank=True,
    )
    product_category = models.OneToOneField(
        to=ProductCategory,
        on_delete=models.RESTRICT,
        related_name='catagorized_products',
        verbose_name=_("Product Category")
    )
    product_discount = models.OneToOneField(
        to=ProductDiscount,
        on_delete=models.RESTRICT,
        related_name='discount_products',
        verbose_name=_("Product Discount"),
        null=True,
        blank=True
    )
    product_colors = models.ManyToManyField(
        to=ProductColor,
        related_name='colored_products',
        verbose_name=_("Product Colors")
    )
    product_tag = models.ManyToManyField(
        to=ProductTag,
        related_name='tagged_products',
        verbose_name=_("Product Tag")
    )
