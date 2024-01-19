from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from tasks.models import Task, TaskPhoto
from tasks.forms import TaskForm, AddTaskPhotoForm


class TaskListView(ListView):
    model = Task 
    template_name = "tasks/task_list.html"
    paginate_by = 20
    context_object_name = "tasks"
    

class TaskDetailView(DetailView):
    model = Task
    template_name = 'tasks/task_detail.html'
    context_object_name = 'task'
    slug_url_kwarg = "task_slug"

    def get_context_data(self, **kwargs):
        slug = self.kwargs.get(self.slug_url_kwarg)
        context = super().get_context_data(**kwargs)
        context["title"] = Task.objects.get(slug=slug)
        return context


class TaskCreateView(CreateView):
    model = Task
    template_name = 'tasks/task_create.html'
    form_class = TaskForm
    success_url = reverse_lazy('task_lists')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def post(self, request):
        form = TaskForm(request.POST)

        if form.is_valid():
            user = form.save()
            messages.success(request, "Task added successful." )
            return redirect("task_lists")
		
        messages.error(request, "Unsuccessful task add. Invalid information.")
    

class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    template_name = 'tasks/task_create.html'
    form_class = TaskForm
    slug_url_kwarg = "task_slug"
    success_url = reverse_lazy('task_lists')

    def get_context_data(self, **kwargs):
        slug = self.kwargs.get(self.slug_url_kwarg)
        context = super().get_context_data(**kwargs)
        context["title"] = Task.objects.get(slug=slug)
        return context

    def get_queryset(self):
        slug = self.kwargs.get(self.slug_url_kwarg)
        queryset = super().get_queryset()
        return queryset.filter(slug=slug)


class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'tasks/task_confirm_delete.html'
    success_url = reverse_lazy('task_lists')
    slug_url_kwarg = "task_slug"
    
    def get_context_data(self, **kwargs):
        slug = self.kwargs.get(self.slug_url_kwarg)
        context = super().get_context_data(**kwargs)
        context["title"] = Task.objects.get(slug=slug)
        return context
    

def add_photo_to_task(request, task_slug):
    if request.method == 'POST':
        form = AddTaskPhotoForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            # photo.task = task
            photo.save()
            messages.success(request, 'Photo added successfully.')
            return redirect('task_detail', task_slug)
    else:
        form = AddTaskPhotoForm()
    return render(request, 'tasks/add_photo.html', {'form': form})