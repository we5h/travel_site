from django.contrib import admin
from django.db.models import Avg
from django.utils.safestring import mark_safe

from .models import BuyTour, Departure, Destination, Rating, Tour


@admin.register(Tour)
class TourAdmin(admin.ModelAdmin):
    """Туры"""
    list_display = ('title',
                    'description',
                    'get_image',
                    'slug',
                    'departure',
                    'price',
                    'stars',
                    'show_average'
                    )
    list_filter = ('departure',)
    search_fields = ('title',
                     'price',
                     'departure__name'
                     )  # чтобы искать по категории надо указать по какому полю категории будем искать  # noqa: E501
    save_on_top = True  # кнопки сохранения сверху
    save_as = True  # добавляется поле 'Сохранить как новый объект'
    readonly_fields = ('slug',
                       'get_image',
                       'show_average',
                       )

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="100" height="110"')

    def show_average(self, obj):
        result = Rating.objects.filter(tour=obj).aggregate(Avg("rating"))
        return result["rating__avg"]

    get_image.short_description = 'Изображение'
    show_average.short_description = "Средний рейтинг"


@admin.register(Departure)
class DepartureAdmin(admin.ModelAdmin):
    """Отправления"""
    list_display = ('name', 'slug',)


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    """Рейтинги"""
    list_display = ('rating', 'tour',)


@admin.register(Destination)
class DestinationAdmin(admin.ModelAdmin):
    """Прибытия"""
    list_display = ('name',)


@admin.register(BuyTour)
class BuyTourAdmin(admin.ModelAdmin):
    """Заказы туров"""
    list_display = ('name', 'email', 'phone', 'tour', 'time', )
    fields = ('name', 'email', 'tour', 'phone',)
