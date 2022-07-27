from django.shortcuts import render
from django.http import HttpResponse
from .models import Child_Info
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.contrib.auth.models import User


def home(request):
    return render(request, 'planner/home.html')


class RecordListView(LoginRequiredMixin, ListView):
    model = Child_Info
    template_name = 'planner/child_table.html'


class RecordDetailView(DetailView):
    model = Child_Info


class RecordCreateView(LoginRequiredMixin, CreateView):
    model = Child_Info
    fields = ['first name', 'last name', 'patronymic', 'id parent', 'birthdate']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class RecordUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
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


class RecordDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Child_Info
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
