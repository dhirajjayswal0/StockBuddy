from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name='home'),
    path('login', views.login, name='login'),
    path('recover', views.recover, name='recover'),
    path('register', views.register, name='register'),
    path('portfolio', views.portfolio, name='Portfolio'),
    path('watchlist', views.watchlist, name='watchlist'),
    path('wallet', views.wallet, name='wallet'),
    path('about', views.about, name='about'),
    path('how_to_use', views.how_to_use, name='how_to_use'),
    path('contact', views.contact, name='contact'),
    path('account', views.account, name='account'),
]