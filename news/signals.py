from django.core.mail import EmailMultiAlternatives
# импортируем сигнал, который будет срабатывать после сохранения объекта в базу данных
from django.db.models.signals import post_save
from django.dispatch import receiver  # импортируем нужный декоратор
from django.shortcuts import redirect
from django.template.loader import render_to_string

# Импорт пользовательских элементов:
# модели - передают ин-ию из БД
from .models import Post, Category
from .views import notify_new_post_in_category

from django.views.decorators.csrf import csrf_exempt