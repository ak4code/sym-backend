from django.db import models

from core.models.mixins import AutoTimestampMixin


class Follow(AutoTimestampMixin):
    follower = models.ForeignKey(
        'core.User',
        on_delete=models.CASCADE,
        related_name='following',
        verbose_name='Подписчик',
    )
    following = models.ForeignKey(
        'core.User',
        on_delete=models.CASCADE,
        related_name='followers',
        verbose_name='Подписан',
    )

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'
        constraints = [
            models.UniqueConstraint(fields=['follower', 'following'], name='unique_follow')
        ]

    def __str__(self):
        return f"{self.follower.email} подписан на {self.following.email}"
