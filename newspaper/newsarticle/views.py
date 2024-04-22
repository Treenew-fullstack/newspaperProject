from django.contrib.auth.decorators import login_required
from django.db.models import Exists, OuterRef
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.http import HttpResponse
from datetime import datetime
from django.views import View
from django.core.cache import cache
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView)
from .models import Post, Subscriber, Category
from .filters import PostFilter
from .forms import PostForm, ArticleForm
import logging


logger = logging.getLogger(__name__)



# Представдение для главной страницы с функциями фильтации
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


# Представдение для просмотра одной новости, статьи
class NewsPreview(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'

    # Переопределение метода получение объекта и условие для кэширования
    def get_object(self, *args, **kwargs):
        obj = cache.get(f'post-{self.kwargs["pk"]}', None)
        if not obj:
            obj = super().get_object(queryset=self.queryset)
            cache.set(f'post-{self.kwargs["pk"]}', obj)
            return obj



# Представдение для страницы создание новостей
class PostCreate(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    raise_exception = True
    permission_required = ('newsarticle.add_post',)
    form_class = PostForm
    model = Post
    template_name = 'create_post.html'

# Автоматическое присвоение типа категории
    def form_valid(self, form):
        post = form.save(commit=False)
        post.category_type = 'NW'
        return super().form_valid(form)


# Представдение для страницы создания статей
class ArticleCreate(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    raise_exception = True
    permission_required = ('newsarticle.add_article',)
    form_class = ArticleForm
    model = Post
    template_name = 'create_article.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.category_type = 'AR'
        return super().form_valid(form)


# Представдение для страницы редактирования статей, новостей
class PostEdit(PermissionRequiredMixin, UpdateView):
    raise_exception = True
    permission_required = ('newsarticle.change_post',)
    form_class = PostForm
    model = Post
    template_name = 'edit_post.html'



# Представдение для страницы удаления статей, новостей
class PostDelete(PermissionRequiredMixin, DeleteView):
    raise_exception = True
    permission_required = ('newsarticle.delete_post',)
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('posts_list')


# Представление для работы с подписками
@login_required
@csrf_protect
def subscriptions(request):
    if request.method == 'POST':
        category_id = request.POST.get('category_id')
        category = Category.objects.get(id=category_id)
        action = request.POST.get('action')

        if action == 'subscribe':
            Subscriber.objects.create(user=request.user, category=category)
        elif action == 'unsubscribe':
            Subscriber.objects.filter(
                user=request.user,
                category=category,
            ).delete()

    categories_with_subscriptions = Category.objects.annotate(
        user_subscribed=Exists(
            Subscriber.objects.filter(
                user=request.user,
                category=OuterRef('pk'),
            )
        )
    ).order_by('naming')
    return render(
        request,
        'subscriptions.html',
        {'categories': categories_with_subscriptions},
    )


# Представление для теста работы Celery-Redis
class IndexView(View):
   def get(self, request):
       hello.delay()
       return HttpResponse('Hello!')







