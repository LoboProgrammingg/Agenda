from django.urls import path

from contact import views

app_name = 'contact'

urlpatterns = [
    path('', views.index, name='index'),  # type:ignore
    path('contact/<int:contact_id>/', views.contact, name='contact'),
    path('search/', views.search, name='search'),   # type:ignore
]