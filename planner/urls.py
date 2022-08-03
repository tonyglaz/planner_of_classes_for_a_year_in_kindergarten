from django.urls import path
from . import views
from .views import (
    ChildRecordListView,
    ChildRecordDetailView,
    ChildRecordDeleteView,
    ChildRecordCreateView,
    ChildRecordUpdateView,
    GroupRecordListView,
)

urlpatterns = [
    path('', GroupRecordListView.as_view(), name='planner-home'),
    path('record/new/', ChildRecordCreateView.as_view(), name='record-create'),
    path('record/<int:pk>/delete/', ChildRecordDeleteView.as_view(), name='record-delete'),
    path('record/<int:pk>/update/', ChildRecordUpdateView.as_view(), name='record-update'),
    path('record/<int:pk>/', ChildRecordListView.as_view(), name='record-detail'),
    # path('register/', views.register, name='register')
]
