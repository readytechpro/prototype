from pathlib import Path
import os
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
def rename_file(sender, instance, **kwargs):
    #change instance filename if it already exists in database by another user
    other_user_images = list(sender.objects.exclude(pk=instance.pk).values_list('image', flat=True))
    if instance.image in other_user_images:
        parent_directory = os.path.dirname(instance.image.name)
        img_basename = os.path.basename(instance.image.name)
        basename_split = list(os.path.splitext(img_basename))
        basename_split[0] = f'{basename_split[0]}_{instance.user.pk}'
        new_filename = os.path.join(parent_directory, ''.join(basename_split))
        instance.image.name = new_filename

@receiver(pre_save, sender=Profile)
def delete_old_image(sender, instance, **kwargs):
    #delete the old profile image before saving a new one
    #don't do anything when creating a new object
    if instance._state.adding and not instance.pk: 
        return False

    #retrieve the current file
    try:
        old_file = sender.objects.get(pk=instance.pk).image
        if old_file.name == 'default.jpg': #don't replace the default image
            return False
    except sender.DoesNotExist:
        return False

    #exit if same filename is being used by another user
    other_user_images = list(sender.objects.exclude(pk=instance.pk).values_list('image', flat=True))
    if old_file in other_user_images:
        return False

    #delete old file if the form is about to save a different file
    if not old_file.name == instance.image.name:
        old_file = storage.open(old_file.name, 'w')
        storage.delete(old_file.name)
        