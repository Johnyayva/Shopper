from django.urls import path, include
from . import views

urlpatterns = [
   path("", views.index, name = "index"),
   path("products/", views.products, name = "products"),
   path("about/", views.about, name = "about"),
   # path("contact/", include("contact_us.urls"), name = "contact"),
   path("logreg/", views.login_register, name = "login_register"),
   path('logout/', views.logout_request, name='logout'),
   path(r'activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/',  views.activate, name='activate'),
]








