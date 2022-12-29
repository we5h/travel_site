from django.urls import path

from . import views

app_name = 'tours'


urlpatterns = [
    path('', views.TourList.as_view(), name='index'),
    path('tour/<slug:slug>/', views.TourDetail.as_view(), name='tour_detail'),
    path('tour/<slug:slug>/buy', views.BuyTourView.as_view(), name='buy_tour'),
    path('departure/<slug:slug>/', views.TourDepartureList.as_view(), name='tour_dep'),
]
