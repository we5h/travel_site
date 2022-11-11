from django.shortcuts import render, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from . models import Tour
# Create your views here.


class TourList(ListView):
    """Список туров на главной странице"""
    model = Tour
    # paginate_by = 9  
    template_name = 'tours/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tours'] = Tour.objects.all()
        return context


class TourDetail(DetailView):
    """Выбран конкретный тур"""
    model = Tour
    template_name = 'tours/tour_detail.html'
    # context_object_name = 'tour'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tour'] = get_object_or_404(Tour)
        return context