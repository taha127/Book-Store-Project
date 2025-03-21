from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


# UserCreationForm -> signup form
# UserChangeForm -> Admin
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'age',)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'age',)
