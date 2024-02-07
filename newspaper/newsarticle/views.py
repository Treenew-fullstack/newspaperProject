from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from datetime import datetime
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView)
from .models import Post
from .filters import PostFilter
from .forms import PostForm, ArticleForm


class PostPreview(ListView):
    model = Post
    ordering = '-date_creation'
    template_name = 'posts.html'
    context_object_name = 'posts'
    paginate_by = 10

#Ниже фукция запроса фильтрации
    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['filterset'] = self.filterset
        context['next_post'] = None
        return context


class NewsPreview(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'

class PostCreate(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    raise_exception = True
    permission_required = ('newsarticle.add_post',)
    form_class = PostForm
    model = Post
    template_name = 'create_post.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.category_type = 'NW'
        return super().form_valid(form)


class ArticleCreate(CreateView):
    permission_required = ('newsarticle.add_article',)
    form_class = ArticleForm
    model = Post
    template_name = 'create_article.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.category_type = 'AR'
        return super().form_valid(form)


class PostEdit(UpdateView):
    permission_required = ('newsarticle.change_post',)
    form_class = PostForm
    model = Post
    template_name = 'edit_post.html'



class PostDelete(DeleteView):
    permission_required = ('newsarticle.delete_post',)
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('posts_list')



