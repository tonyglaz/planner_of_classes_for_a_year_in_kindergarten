from django.urls import path
from . import views
from .views import (
    RecordListView,
    RecordDetailView,
    RecordDeleteView,
    RecordCreateView,
    RecordUpdateView,
)

urlpatterns = [
    path('', RecordListView.as_view(), name='planner-home'),
    path('record/new/', RecordCreateView.as_view(), name='record-create'),
    path('record/<int:pk>/delete/', RecordDeleteView.as_view(), name='record-delete'),
    path('record/<int:pk>/update/', RecordUpdateView.as_view(), name='record-update'),
    path('record/<int:pk>/', RecordDetailView.as_view(), name='record-detail'),
    # path('register/', views.register, name='register')
]
