from django.urls import path
from . import views

urlpatterns = [
    path('', views.my_view, name='my_view'),
    path('record/<int:record_id>/', views.get_single_record, name='single_record'),
    path('record/list/', views.get_records_list, name='record_list'),
    path('events/chronological/', views.chronological_list, name='chronological_list'),
]
