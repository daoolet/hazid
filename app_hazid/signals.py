from app_users.models import CustomUser, AllowedUser
from django.db.models.signals import pre_delete
from django.dispatch import receiver

@receiver(pre_delete, sender=AllowedUser)
def delete_related_custom_user(sender, instance, **kwargs):
    try:
        custom_user = CustomUser.objects.get(email=instance.email)
        custom_user.delete()
    except CustomUser.DoesNotExist:
        pass