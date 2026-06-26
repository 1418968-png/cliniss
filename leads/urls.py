from django.urls import path

from . import views

app_name = 'leads'

urlpatterns = [
    path('leads/submit', views.submit_lead, name='submit'),
]
