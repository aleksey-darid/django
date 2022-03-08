"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_framework.routers import SimpleRouter

from Front.views import home_app, base_app
from Products.views import SuppliersView, ProductionView, BidView, supply_app, suppliers_app, \
    production_app, bid_app, SupplyView
from Users.views import UsersView, WorkersView, AdministrationView, users_app, workers_app, administration_app, \
    login_app, registration_app
from HR.views import ScheduleView, schedule_app

router = SimpleRouter()
router.register("api/supply", SupplyView)
router.register("api/suppliers", SuppliersView)
router.register("api/production", ProductionView)
router.register("api/bid", BidView)
router.register("api/users", UsersView)
router.register("api/workers", WorkersView)
router.register("api/administration", AdministrationView)
router.register("api/schedule", ScheduleView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('supply_page/', supply_app),
    path('suppliers_page/', suppliers_app),
    path('production_page/', production_app),
    path('bid_page/', bid_app),
    path('schedule_page/', schedule_app),
    path('users_page/', users_app),
    path('workers_page/', workers_app),
    path('administration_page/', administration_app),
    path('login_page/', login_app),
    path('base_page/', base_app),
    path('registration_page/', registration_app),
    path('', home_app)
]

urlpatterns += router.urls
