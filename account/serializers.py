
from rest_framework import serializers
from .models import User


class AccountSerializer(serializers.ModelSerializer):

    """
    Serializer for handling user account creation.

    This serializer is used to validate and process the input data provided during user account creation.

    Fields:
        email (EmailField): The email address associated with the user account.
        username (CharField): The username for the user account.
        mobile (CharField): The mobile number associated with the user account.
        password (CharField): The password for the user account.

    Methods:
        create(validated_data):
            Override the create method to use the create_user method for creating a new user instance.

    Example:
        To create a new user account:
        ```json
        {
            "email": "user@example.com",
            "username": "new_user",
            "mobile": "1234567890",
            "password": "password123"
        }
        ```

    Notes:
        - The create method is overridden to use the create_user method of the User model for creating a new user.
        - This serializer is used in conjunction with the AccountCreateAPI to handle user account creation.

    """
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['email', 'username', 'mobile', 'password', ]
    def create(self, validated_data):
        """
         We need to override create method from ModelSerializer. beacause 
         this method use create method for create new models of instance.
         but our User Model we have created function create_user and it is set_password use
         hashing. and create method is not use set_password
         it is save models like this... 
         create(usename = username, password =password)
        """
        username = validated_data.get("username")
        email = validated_data.get("email")
        mobile = validated_data.get("mobile")
        password = validated_data.get("password")
        user = User.objects.create_user(
                    email=email,
                    username=username, 
                    mobile=mobile,
                    password=password
               )
        return user


