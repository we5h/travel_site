from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse


class Destination(models.Model):
    """Города прибытия"""
    name = models.CharField(max_length=50 , verbose_name="Город прибытия")

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Прибытие"
        verbose_name_plural = "Прибытия"

class Departure(models.Model):
    """Города отправлений"""
    CITIES = [
        ("Из Москвы", "Из Москвы"),
        ("Из Петербурга", "Из Петербурга"), 
        ("Из Новосибирска", "Из Новосибирска"),
        ("Из Екатеринбурга", "Из Екатеринбурга"),
        ("Из Казани", "Из Казани"),
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
        ('1', 1),
        ('2', 2),
        ('3', 3),
        ('4', 4),
        ('5', 5)
    ]

    title = models.CharField(max_length=155, verbose_name="Название")
    description = models.TextField(max_length=6000, verbose_name="Описание")
    slug = models.SlugField(max_length=130, unique=True, null=True)
    departure = models.ForeignKey(Departure, related_name='tours', on_delete = models.SET_NULL, null=True, verbose_name="Город отправления")
    destination = models.ForeignKey(Destination, related_name='tours', on_delete = models.SET_NULL, null=True, verbose_name="Город прибытия")
    image = models.ImageField(upload_to='images/', blank=True, verbose_name="Изображение")
    price = models.PositiveIntegerField(verbose_name="Цена")
    stars = models.CharField(max_length=5, choices=STARS, default='OS', verbose_name="Кол-во звёзд")
    nights = models.PositiveIntegerField(null=True, verbose_name="Кол-во ночей")
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name="Время публикации тура")

    def __str__(self) -> str:
        return self.title

    def save(self, *args, **kwargs):
        """Автоматический слаг"""
        if not self.id:
            self.slug = slugify(self.title)
        super(Tour, self).save(*args, **kwargs)

    def get_absolute_url(self):     
        return reverse('tours:tour_detail', kwargs={'slug' : self.slug})

    class Meta:
        verbose_name = "Тур"
        verbose_name_plural = "Туры"
        ordering = ['-pub_date']


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


class BuyTour(models.Model):
    """Форма покупки тура"""
    name = models.CharField(max_length=120, verbose_name="Имя")
    email = models.EmailField(max_length=120, blank=True, null=True, verbose_name="Email")
    phone = models.CharField(max_length=12, verbose_name="Номер телефона")
    tour = models.ForeignKey(Tour, on_delete = models.SET_NULL, null=True, verbose_name="Выбранный тур")
    time = models.DateTimeField(auto_now_add=True, verbose_name="Время оформления заказа")

    def __str__(self) -> str:
        return f'{self.name} - {self.phone}'
    
    class Meta:
        verbose_name = "Заказ тура"
        verbose_name_plural = "Заказы туров"
        ordering = ['-time']