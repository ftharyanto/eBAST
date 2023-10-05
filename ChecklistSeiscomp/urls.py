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
    path('export_excel/<int:id>', views.export_excel, name='export_excel'),
    path('detail_view/<int:id>', views.detail_view, name='detail_view'),
    path('export_pdf_instant/', views.export_pdf_instant, name='export_pdf_instant'),
    path('send_to_gcp_ss/', views.send_to_gcp_ss, name='send_to_gcp_ss'),
    path('station_list_view', views.station_list_view, name='station_list_view'),
    path('station_list_delete/<int:id>/', views.station_list_delete, name='station_list_delete'),
]
