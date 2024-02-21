from django.core.mail import EmailMultiAlternatives
from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from .models import PostCategory





# Сигнал для отправки и отправка подписчикам сообщения электронной почты после появления нового поста
@receiver(m2m_changed, sender=PostCategory)
def post_created_notify(sender, instance, **kwargs):
    if kwargs['action'] == 'post_add':
        categories = instance.post_category.all()
        subscribers_emails = []

        for cat in categories:
            subscribers = cat.subscribers.all()
            subscribers_emails += [s.email for s in subscribers]

        subject = f'Новая статья в категории {cat}'

        text_content = (
        f'Категория: {cat}\n'
        f'Название статьи: {instance.title}\n \n'
        f'Прочитать данную можно тут: http://127.0.0.1:8000{instance.get_absolute_url()}'
        )
        html_content = (
        f'Категория: {cat}<br>'
        f'Название статьи: {instance.title}<br><br>'
        f'Прочитать данную можно <a href="http://127.0.0.1:8000{instance.get_absolute_url()}">'
        f'тут:</a>'
        )

        for email in subscribers_emails:
            msg = EmailMultiAlternatives(subject, text_content, None, [email])
            msg.attach_alternative(html_content, 'text/html')
            msg.send()





























        # emails = User.objects.filter(
        #     catigories=instance.post_category(id)
        # ).values_list('email', flat=True)
        #
        # subject = f'Новая статья в категории {instance.post_category}'
        #
        # text_content = (
        # f'Тип: {instance.category_type}\n'
        # f'Категория: {instance.post_category}\n'
        # f'Название статьи: {instance.title}\n \n'
        # f'Прочитать данную можно тут: http://127.0.0.1:8000{instance.get_absolute_url()}'
        # )
        # html_content = (
        # f'Тип: {instance.category_type}<br>>'
        # f'Категория: {instance.post_category}<br>'
        # f'Название статьи: {instance.title}<br><br>'
        # f'Прочитать данную можно <a href="http://127.0.0.1:8000{instance.get_absolute_url()}">'
        # f'тут:</a>'
        # )
        #
        # for email in emails:
        #     msg = EmailMultiAlternatives(subject, text_content, None, [email])
        #     msg.attach_alternative(html_content, 'text/html')
        #     msg.send()

