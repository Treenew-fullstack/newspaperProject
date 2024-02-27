import datetime
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from celery import shared_task
from .models import Post, Category


@shared_task
def email_notify(pk):
    post = Post.objects.get(pk=pk)
    categories = post.post_category.all()
    subscribers_emails = []

    for cat in categories:
        subscribers = cat.subscribers.all()
        subscribers_emails += [s.email for s in subscribers]

        subject = f'Новая статья в категории {cat}'

        text_content = (
        f'Категория: {cat}\n'
        f'Название статьи: {post.title}\n \n'
        f'Прочитать данную можно тут: http://127.0.0.1:8000{post.get_absolute_url()}'
        )
        html_content = (
        f'Категория: {cat}<br>'
        f'Название статьи: {post.title}<br><br>'
        f'Прочитать данную можно <a href="http://127.0.0.1:8000{post.get_absolute_url()}">'
        f'тут:</a>'
        )

        for email in subscribers_emails:
            msg = EmailMultiAlternatives(subject, text_content, None, [email])
            msg.attach_alternative(html_content, 'text/html')
            msg.send()


@shared_task
def weekly_send_notify():
    today = datetime.datetime.now()
    last_week = today - datetime.timedelta(days=7)
    posts = Post.objects.filter(date_creation__gt=last_week)
    categories = set(posts.values_list('post_category__naming', flat=True))
    subscribers = set(Category.objects.filter(naming__in=categories).values_list('subscribers__email', flat=True))

    html_content = render_to_string(
        'weekly_post.html',
        {
            'link': 'http://127.0.0.1:8000',
            'posts': posts,
        }
    )
    msg = EmailMultiAlternatives(
        subject='Статьи за неделю',
        body='',
        from_email='treenew2@yandex.ru',
        to=subscribers,
    )
    msg.attach_alternative(html_content, 'text/html')
    msg.send()
