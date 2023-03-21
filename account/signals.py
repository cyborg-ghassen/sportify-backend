from django.contrib.auth.models import Group
from django.db.models.signals import post_save
from django.dispatch import receiver

from account.models import ClubUser


@receiver(post_save, sender=ClubUser)
def update_user_group(sender, instance, created, **kwargs):
    if created:
        group = Group.objects.get_or_create(name="Visitor")[0]
        instance.groups.add(group)
        instance.save()
