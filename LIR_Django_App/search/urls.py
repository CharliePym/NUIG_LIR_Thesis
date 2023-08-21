from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='home'),
    path('search/', views.search_page, name='search'),
    path('about/', views.about_page, name='about'),
    path('results/', views.results_page, name='results'),
    path('judgment/', views.judgment_page, name='judgment'),
    path('judgment/<int:judgment_id>/', views.judgment_page, name='judgment'),
]
