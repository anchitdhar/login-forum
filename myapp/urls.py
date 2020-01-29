from django.urls import path
from . import views


urlpatterns = [
    path('',views.indexView,name="home"),
    path('dashboard/',views.dashboardView,name="Dashboard"),
    # path('login/',),
    path('register/',views.registerView,name = "register_url"),
    # path('logout/',),
]