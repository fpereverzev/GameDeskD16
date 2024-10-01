from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.mail import send_mail
from django.conf import settings
from .models import Ad, Reply
from .forms import AdForm, ReplyForm

User = get_user_model()

# Представление для регистрации пользователей
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Отправка уведомления на почту
            send_mail(
                'Добро пожаловать!',
                'Вы успешно зарегистрированы на нашем сайте.',
                settings.DEFAULT_FROM_EMAIL,
                [user.email],
                fail_silently=False,
            )
            messages.success(request, 'Вы успешно зарегистрированы! Теперь вы можете войти.')
            return redirect('login')  # Перенаправление на страницу входа
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

# Представление для списка всех объявлений
def ad_list(request):
    ads = Ad.objects.all().order_by('-created_at')
    return render(request, 'ads/ad_list.html', {'ads': ads})

# Представление для детального просмотра объявления
def ad_detail(request, pk):
    ad = get_object_or_404(Ad, pk=pk)
    replies = ad.replies.all()
    if request.method == 'POST' and request.user.is_authenticated:
        form = ReplyForm(request.POST)
        if form.is_valid():
            reply = form.save(commit=False)
            reply.ad = ad
            reply.author = request.user
            reply.save()
            messages.success(request, 'Ваш отклик успешно добавлен.')
            return redirect('ad_detail', pk=ad.pk)
    else:
        form = ReplyForm()
    return render(request, 'ads/ad_detail.html', {'ad': ad, 'replies': replies, 'form': form})

# Представление для создания нового объявления
@login_required
def ad_create(request):
    if request.method == 'POST':
        form = AdForm(request.POST)
        if form.is_valid():
            ad = form.save(commit=False)
            ad.author = request.user
            ad.save()
            messages.success(request, 'Объявление успешно создано.')
            return redirect('ad_detail', pk=ad.pk)
    else:
        form = AdForm()
    return render(request, 'ads/ad_form.html', {'form': form})

# Представление для редактирования объявления
@login_required
def ad_edit(request, pk):
    ad = get_object_or_404(Ad, pk=pk, author=request.user)
    if request.method == 'POST':
        form = AdForm(request.POST, instance=ad)
        if form.is_valid():
            form.save()
            messages.success(request, 'Объявление успешно отредактировано.')
            return redirect('ad_detail', pk=ad.pk)
    else:
        form = AdForm(instance=ad)
    return render(request, 'ads/ad_form.html', {'form': form})

# Представление для управления откликами
@login_required
def user_replies(request):
    replies = Reply.objects.filter(author=request.user).select_related('ad')
    return render(request, 'ads/user_replies.html', {'replies': replies})

