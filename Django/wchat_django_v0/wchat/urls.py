"""wchat URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from analysis.views import App_view, Cover, Page1_1, Page1_2, Page2_1, Page2_2, Page2_3, Page3_1, Page3_2, Page4_1, Page4_2, Page4_3, Contact_us

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app_view/', App_view),
    path('cover/', Cover),
    path('page1_1/', Page1_1),
    path('page1_2/', Page1_2),
    path('page2_1/', Page2_1),
    path('page2_2/', Page2_2),
    path('page2_3/', Page2_3),
    path('page3_1/', Page3_1),
    path('page3_2/', Page3_2),
    path('page4_1/', Page4_1),
    path('page4_2/', Page4_2),
    path('page4_3/', Page4_3),
    path('contact_us/', Contact_us)
]
