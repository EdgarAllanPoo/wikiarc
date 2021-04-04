from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home_view'),
    path('page1/', views.page1_view, name='networking'),
    path('pingcmd/', views.page2_view, name='pingcmd'),
    path('ipsatujaringan/', views.page3_view, name='ipsatujaringan'),
    path('serverdatabaseclient/', views.page4_view, name='serverdatabaseclient'),
    path('konfigurasiip/', views.page4_view, name='konfigurasiip'),
    path('create/', views.create_page_view, name='create_page'),
]
