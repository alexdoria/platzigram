from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from users.models import Profile


# Forms by class for users app
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UpdateProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['website', 'biography', 'phone_number', 'profile_picture']
