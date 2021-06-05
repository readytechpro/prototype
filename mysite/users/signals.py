from django.db.models.signals import post_save, pre_save
from django.contrib.auth.models import User #sender
from django.dispatch import receiver
from .models import Profile
from django.core.files.storage import default_storage as storage

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    #create a new profile every time a new user is created
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    #save the profile every time a user is saved
    instance.profile.save()

@receiver(pre_save, sender=Profile)
def delete_old_image(sender, instance, **kwargs):
    #delete the old profile image before saving a new one
    #don't do anything when creating a new object
    if instance._state.adding and not instance.pk: 
        return False

    #retrieve the current file
    try:
        old_file = storage.open(sender.objects.get(pk=instance.pk).image.name, "w")
        if old_file.name == 'default.jpg': #don't replace the default image
            old_file.close()
            return False
    except sender.DoesNotExist:
        return False

    #save new file, delete old file if it isn't the same file
    new_file = storage.open(instance.image.name, "w")
    if not old_file.name == new_file.name:
        storage.delete(old_file.name)
        new_file.close()
    else:
        old_file.close()
        new_file.close()
