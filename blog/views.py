from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.urls import reverse_lazy
from .models import Post
from .forms import PostForm
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin



class BlogListView(ListView):
    model = Post
    template_name = 'blog/home.html'


class BlogDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    #content_objct_name = 'post'

    
class BlogCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_new.html'
    success_message = "%(field)s - criado com sucesso"
    
    def form_valid(self, form):
        object = form.save(commit=False)
        object.autor = self.request.user
        object.save()
        return super().form_valid(form)

    def get_success_message(self, cleaned_data):
            return self.success_message % dict(
            cleaned_data,
            field=self.object.titulo,
        )
    
class BlogEditView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_edit.html'
    #fields = ('titulo', 'conteudo')
    success_message = "%(field)s - alterado com sucesso"
    
    def form_valid(self, form):
        object = form.save(commit=False)
        object.autor = self.request.user
        object.save()
        return super().form_valid(form)
    
    def get_success_message(self, cleaned_data):
            return self.success_message % dict(
            cleaned_data,
            field=self.object.titulo,
        )
    
class BlogDeleteView(SuccessMessageMixin, DeleteView):
    model = Post
    template_name = 'blog/post_delete.html'
    success_url = reverse_lazy("home")
    
    success_message = "Deletado com sucesso"
    
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(BlogDeleteView, self).delete(request, *args, **kwargs)