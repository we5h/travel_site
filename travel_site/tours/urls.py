from django.urls import path

from . import views

app_name = 'tours'


urlpatterns = [
    path('', views.TourList.as_view(), name='index'),
    path('tour/<slug:slug>/', views.TourDetail.as_view(), name='tour_detail'),
    # path('departure/<slug:slug>/', views.group_posts, name='group_list'),
    path('buy_tour/', views.BuyTourView.as_view(), name='buy_tour'),
]
