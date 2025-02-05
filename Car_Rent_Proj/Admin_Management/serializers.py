# from rest_framework import serializers
# from .models import AdminUser

# class AdminUserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = AdminUser
#         fields = '__all__'  # Include all fields or specify them as needed




# from rest_framework import serializers
# from .models import AdminUser

# class AdminUserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = AdminUser
#         fields = ['id', 'username', 'email', 'is_staff', 'is_superuser']  # Specify only the necessary fields
#         read_only_fields = ['id']  # Example: make 'id' read-only if it's auto-generated

#     def validate_email(self, value):
#         """Check that the email is valid and unique."""
#         if AdminUser.objects.filter(email=value).exists():
#             raise serializers.ValidationError("This email is already in use.")
#         return value

#     def create(self, validated_data):
#         """Override create method to handle password hashing."""
#         user = AdminUser(**validated_data)
#         user.set_password(validated_data['password'])  # Assuming you have a password field
#         user.save()
#         return user


from rest_framework import serializers
from .models import AdminUser
from django.contrib.auth.models import User

class AdminUserSerializer(serializers.ModelSerializer):
    # You can also serialize related User fields if needed
    username = serializers.CharField(source='user.username')
    email = serializers.EmailField(source='user.email')

    class Meta:
        model = AdminUser
        fields = ['id', 'username', 'email', 'is_super_admin']  # Include relevant fields

    def create(self, validated_data):
        user_data = validated_data.pop('user')  # Extract user data
        user = User(**user_data)  # Create User instance
        user.set_password(user_data.get('password'))  # Hash the password
        user.save()  # Save User instance

        admin_user = AdminUser.objects.create(user=user, **validated_data)  # Create AdminUser instance
        return admin_user

    def validate_email(self, value):
        """Check that the email is valid and unique."""
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("This email is already in use.")
        return value
