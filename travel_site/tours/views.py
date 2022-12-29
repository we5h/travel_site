from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.contrib import messages
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger

from bootstrap_modal_forms.generic import BSModalCreateView

from . models import Tour, BuyTour, Departure
from . forms import BuyTourForm
# Create your views here.


class TourList(ListView):
    """Список туров на главной странице"""
    model = Tour
    paginate_by = 6  
    template_name = 'tours/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tour_list = Tour.objects.all()
        dep_list = Departure.objects.all()
        paginator = Paginator(tour_list, self.paginate_by)

        page = self.request.GET.get('page')

        try:
            tours = paginator.page(page)
        except PageNotAnInteger:
            tours = paginator.page(1)
        except EmptyPage:
            tours = paginator.page(paginator.num_pages)
        context['tours'] = tours
        context['departures'] = dep_list
        return context


class TourDepartureList(ListView):
    """Список туров по отправлениям"""
    model = Tour
    paginate_by = 6  
    template_name = 'tours/tours_departure.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tour_list = Tour.objects.filter(departure__slug=self.kwargs.get("slug"))
        dep_list = Departure.objects.all()
        paginator = Paginator(tour_list, self.paginate_by)

        page = self.request.GET.get('page')

        try:
            tours = paginator.page(page)
        except PageNotAnInteger:
            tours = paginator.page(1)
        except EmptyPage:
            tours = paginator.page(paginator.num_pages)
        context['tours'] = tours
        context['departures'] = dep_list
        return context

class TourDetail(DetailView):
    """Выбран конкретный тур"""
    model = Tour
    template_name = 'tours/tour_detail.html'
    slug_url_kwarg = 'slug'
    # context_object_name = 'tour'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tour'] = get_object_or_404(Tour , slug=self.kwargs.get("slug"))
        return context


class BuyTourView(BSModalCreateView):
    """Покупка тура"""
    template_name = 'modal_forms/buy_tour.html'
    form_class = BuyTourForm
    success_url = reverse_lazy('tours:index')

    def get_initial(self):
        """Прокинули выбранный тур"""
        tour = get_object_or_404(Tour, slug=self.kwargs.get('slug'))
        return {
            'tour':tour,
        }

    def form_valid(self, form):
        """Success_message в этой библиотеке не работает, поэтому этот костыль спас нас"""
        if not self.request.headers.get('x-requested-with') == 'XMLHttpRequest':
            messages.success(self.request, "Заказ принят.Менеджер свяжется с вами в ближайшее время.")

        return super().form_valid(form)