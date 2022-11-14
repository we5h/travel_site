from django.shortcuts import render, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.contrib import messages

from bootstrap_modal_forms.generic import BSModalCreateView

from . models import Tour, BuyTour
from . forms import BuyTourForm
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


class BuyTourView(BSModalCreateView):
    """Покупка тура"""
    template_name = 'modal_forms/buy_tour.html'
    form_class = BuyTourForm
    success_url = reverse_lazy('tours:index')

    def form_valid(self, form):
        """Success_message в этой библиотеке не работает, поэтому этот костыль спас нас"""
        if not self.request.headers.get('x-requested-with') == 'XMLHttpRequest':
            messages.success(self.request, "Заказ принят.Менеджер свяжется с вами в ближайшее время.")

        return super().form_valid(form)