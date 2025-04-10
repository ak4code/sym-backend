from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from core.models import User, Follow


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    """Админка пользователя"""

    list_display = ('email', 'is_active', 'is_staff', 'is_superuser', 'last_login')
    list_filter = ('is_active', 'is_staff', 'is_superuser')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Персональная информация', {'fields': ()}),
        ('Разрешения', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Важные даты', {'fields': ('last_login', 'created_at', 'updated_at')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_active', 'is_staff', 'is_superuser')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ('groups', 'user_permissions')
    readonly_fields = ('created_at', 'updated_at', 'last_login')


@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    """Админка подписок"""
    list_display = ('__str__', 'created_at')
    list_select_related = ('follower', 'following')
    raw_id_fields = ('follower', 'following')
    search_fields = ('follower__email', 'following__email')
