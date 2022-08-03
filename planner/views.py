from django.shortcuts import render
from django.http import HttpResponse
from .models import Child_Info, Group_Info, Parent_Info
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.contrib.auth.models import User


class GroupRecordListView(LoginRequiredMixin, ListView):
    model = Group_Info
    template_name = 'planner/groups.html'
    context_object_name = 'groups_records'


class ChildRecordListView(LoginRequiredMixin, ListView):
    model = Child_Info
    template_name = 'planner/home.html'
    context_object_name = 'child_records'


class ChildRecordDetailView(DetailView):
    model = Child_Info


class ChildRecordCreateView(LoginRequiredMixin, CreateView):
    model = Child_Info
    fields = ['first name', 'last name', 'patronymic', 'id parent', 'birthdate']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ChildRecordUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Child_Info
    fields = ['first name', 'last name', 'patronymic', 'id parent', 'birthdate']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class ChildRecordDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Child_Info
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
