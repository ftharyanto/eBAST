"""eBAST URL Configuration

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
from ChecklistSeiscomp import views

app_name = 'ChecklistSeiscomp'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.create_view, name='checklist-seiscomp'),
    path('checklist-seiscomp', views.create_view, name='checklist-seiscomp'),
    path('checklist-seiscomp/list_view', views.list_view, name='list_view'),
    path('checklist-seiscomp/operator_view', views.operator_view, name='operator_view'),
    path('checklist-seiscomp/operator_delete/<int:id>/', views.operator_delete, name='operator_delete'),
    path('checklist-seiscomp/operator_update/<int:id>/', views.operator_update, name='operator_update'),
    path('checklist-seiscomp/data_delete/<int:id>/', views.data_delete, name='data_delete'),
]
