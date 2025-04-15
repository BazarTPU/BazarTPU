from .models import CustomUser
from django.contrib.auth.forms import UserChangeForm


class ProfileEditForm(UserChangeForm):
    password = None

    class Meta:
        model = CustomUser
        fields = ('phone', 'telegram', 'dormitory', 'profile_photo')