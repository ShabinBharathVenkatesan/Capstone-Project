from django import forms
from django.contrib.auth.models import User
from .models import AdminUser

class AdminUserForm(forms.ModelForm):
    class Meta:
        model = AdminUser
        fields = ['user', 'is_super_admin']  # Include any additional fields as necessary

    def __init__(self, *args, **kwargs):
        super(AdminUserForm, self).__init__(*args, **kwargs)
        self.fields['user'].queryset = User.objects.all()  # Limit choices to existing users
