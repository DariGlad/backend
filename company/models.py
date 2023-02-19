from django.core.exceptions import ValidationError
from django.db import models


class Products(models.Model):
    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    title = models.CharField(max_length=60, verbose_name='Название товара')
    model = models.CharField(max_length=100, verbose_name='Модель товара')
    release_date = models.DateField(verbose_name='Дата выхода на рынок')

    def __str__(self):
        return self.title


class Contact(models.Model):
    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'

    email = models.EmailField(max_length=254, unique=True)
    country = models.CharField(max_length=100, verbose_name='Страна')
    city = models.CharField(max_length=200, verbose_name='Город')
    street = models.CharField(max_length=200, verbose_name='Улица')
    house_number = models.CharField(max_length=200, verbose_name='Номер дома')

    def __str__(self):
        return self.email


class Company(models.Model):
    class Meta:
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'

    class LevelHierarchy(models.IntegerChoices):
        factory = 0, 'Завод'
        retail = 1, 'Розничная сеть'
        entrepreneur = 2, 'Индивидуальный предприниматель'

    title = models.CharField(max_length=100, unique=True, verbose_name='Название компании')
    hierarchy = models.SmallIntegerField(choices=LevelHierarchy.choices, verbose_name='уровень иерархии')
    contacts = models.OneToOneField(
        'company.Contact',
        on_delete=models.CASCADE,
        related_name='company',
        verbose_name='Контактные данные'
    )
    products = models.ManyToManyField(
        'company.Products',
        related_name='company',
        blank=True,
        verbose_name='Товар'
    )
    provider = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        related_name='trader',
        verbose_name='Поставщик',
        null=True,
        blank=True
    )
    debt = models.DecimalField(
        max_digits=25,
        decimal_places=2,
        verbose_name='Задолженность',
        default=0
    )
    create_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Время создания'
    )

    def __str__(self):
        return self.title

    def clean(self):
        if self.provider:
            if self.provider.id == self.id:
                raise ValidationError('Компания не может быть своим поставщиком')
