from django.db import models
from django.template.defaultfilters import slugify


class Departure(models.Model):
    """Города отправлений"""
    CITIES = [
        ("msk", "Из Москвы"),
        ("spb", "Из Петербурга"), 
        ("nsk", "Из Новосибирска"),
        ("ekb", "Из Екатеринбурга"),
        ("kazan", "Из Казани"),
    ]
    name = models.CharField(max_length=50 ,choices=CITIES, verbose_name="Город отправления")
    slug = models.SlugField(max_length=130, unique=True, null=True)

    def __str__(self) -> str:
        return self.name

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(Departure, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Отправление"
        verbose_name_plural = "Отправления"


class Tour(models.Model):
    """Туры"""
    STARS = [
        ('OS', 1),
        ('TWS', 2),
        ('THRS', 3),
        ('FOURS', 4),
        ('FIVS', 5)
    ]

    title = models.CharField(max_length=155, verbose_name="Название")
    description = models.TextField(max_length=6000, verbose_name="Описание")
    slug = models.SlugField(max_length=130, unique=True, null=True)
    departure = models.ForeignKey(Departure, related_name='tours', on_delete = models.SET_NULL, null=True, verbose_name="Город отправления")
    image = models.ImageField(upload_to='images/', blank=True, verbose_name="Изображение")
    price = models.PositiveIntegerField(verbose_name="Цена")
    stars = models.CharField(max_length=5, choices=STARS, default='OS', verbose_name="Кол-во звёзд")

    def __str__(self) -> str:
        return self.title

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        super(Tour, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Тур"
        verbose_name_plural = "Туры"


class Rating(models.Model):
    """
    Установка рейтинга:
    будет выводиться средний рейтинг на тур
    """
    rating = models.PositiveSmallIntegerField(null=True, verbose_name="Рейтинг")
    tour = models.ForeignKey(Tour, related_name='ratings', on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = "Рейтинг"
        verbose_name_plural = "Рейтинги"
