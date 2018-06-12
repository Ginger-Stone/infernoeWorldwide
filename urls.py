from django.urls import path
from . import views
from infernoeWorldwide.models import Portfolio
from django.views.generic import ListView, DetailView
##from infernoeWorldwide.views import PortfolioList, PortfolioDetail

app_name = 'infernoeWorldwide'
urlpatterns = [
        path('', views.index, name='index'),
      ##  path('index/service/', views.index, name='service'),
       ## path('index/portfolio/', PortfolioList.as_view(), name='portfolio'),
        ##path('index/portfolio/<slug>/', PortfolioDetail.as_view(), name='portfolioDetail'),
        
] 

