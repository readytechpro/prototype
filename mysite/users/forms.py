from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']

    def clean_image(self):
        MAX_BYTES = 6 * 1024 * 1024
        image = self.cleaned_data['image']
        file_size = image.size
        if file_size > MAX_BYTES:
            raise ValidationError(
                f'Image too large to upload. The maximum upload size is \
                    {(MAX_BYTES / 1024 / 1024):.2f} MB, and your \
                    {(file_size / 1024 / 1024):.2f} MB image exceeds that \
                    limit. Navigate to this page to try again.'
                )
        else:
            return image
