from django.urls import path

from . import views

app_name = 'pages'

urlpatterns = [
    path('', views.page_detail, name='home'),
    path('favicon.ico', views.favicon_ico, name='favicon'),
    path('service-worker.js', views.service_worker_js, name='service-worker'),
    path('search', views.search, name='search'),
    path('search/', views.search_trailing_slash, name='search-trailing-slash'),
    path('robots.txt', views.robots_txt, name='robots'),
    path('sitemap.xml', views.sitemap_xml, name='sitemap'),
    path('<slug:slug>/', views.page_detail_trailing_slash, name='detail-trailing-slash'),
    path('<slug:slug>', views.page_detail, name='detail'),
]
