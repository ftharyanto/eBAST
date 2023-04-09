from django.urls import path
from . import views

app_name = 'ChecklistSeiscomp'

urlpatterns = [
    path('', views.create_view, name='home'),
    path('statistic_view/', views.statistic_view, name='statistic_view'),
    path('create_view/', views.create_view, name='create_view'),
    path('list_view', views.list_view, name='list_view'),
    path('operator_view', views.operator_view, name='operator_view'),
    path('operator_delete/<int:id>/', views.operator_delete, name='operator_delete'),
    path('operator_update/<int:id>/', views.operator_update, name='operator_update'),
    path('data_delete/<int:id>/', views.data_delete, name='data_delete'),
    path('export_excel_instant/', views.export_excel_instant, name='export_excel_instant'),
    path('station_list_view', views.station_list_view, name='station_list_view'),
    path('station_list_delete/<int:id>/', views.station_list_delete, name='station_list_delete'),
]
