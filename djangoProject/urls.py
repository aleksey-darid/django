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

import Front.views
from Front.views import home_app, base_app
from Products.views import SuppliersView, ProductionView, BidView, supply_app, suppliers_app, \
    production_app, bid_app, SupplyView
from Users.views import UserView, user_app, \
    login_app, logout_app, registration_app, workers_app
from HR.views import ScheduleView, schedule_app, wages_app

router = SimpleRouter()
router.register("api/supply", SupplyView)
router.register("api/suppliers", SuppliersView)
router.register("api/production", ProductionView)
router.register("api/bid", BidView)
router.register("api/users", UserView)
router.register("api/schedule", ScheduleView)

urlpatterns = [
    path('admin/', admin.site.urls, name="admin"),
    path('supply_page/', supply_app, name="supply"),
    path('suppliers_page/', suppliers_app, name="suppliers"),
    path('production_page/', production_app, name="production"),
    path('bid_page/', bid_app, name="bid"),
    path('schedule_page/', schedule_app, name="schedule"),
    path('users_page/', user_app, name="users"),
    path('workers_page/', workers_app, name="workers"),
    path('login_page/', login_app, name="login"),
    path('logout_page/', logout_app, name="logout"),
    path('base_page/', base_app, name="base"),
    path('registration_page/', registration_app, name="registration"),
    path('wages_page/', wages_app, name="wages"),
    path('', home_app, name='home')
]

urlpatterns += router.urls
