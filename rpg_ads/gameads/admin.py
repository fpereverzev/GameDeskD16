from django.contrib import admin
from .models import Ad, Reply, OneTimeCode


@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'created_at')  # Поля, отображаемые в списке
    search_fields = ('title', 'content', 'author__username')  # Поля для поиска
    list_filter = ('category', 'created_at')  # Фильтры для админки
    ordering = ('-created_at',)  # Сортировка по дате создания (новые сверху)


@admin.register(Reply)
class ReplyAdmin(admin.ModelAdmin):
    list_display = ('ad', 'author', 'created_at', 'accepted')  # Поля, отображаемые в списке
    search_fields = ('ad__title', 'author__username', 'content')  # Поля для поиска
    list_filter = ('accepted', 'created_at')  # Фильтры для админки
    ordering = ('-created_at',)  # Сортировка по дате создания (новые сверху)


@admin.register(OneTimeCode)
class OneTimeCodeAdmin(admin.ModelAdmin):
    list_display = ('email', 'code', 'created_at')  # Поля, отображаемые в списке
    search_fields = ('email',)  # Поля для поиска
    ordering = ('-created_at',)  # Сортировка по дате создания (новые сверху)
