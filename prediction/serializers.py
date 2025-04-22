# from rest_framework import serializers
# from .models import UserModel

from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserProfile

class PredictionSerializer(serializers.Serializer):
    question1 = serializers.CharField(max_length=100)
    question2 = serializers.CharField(max_length=100)
    question3 = serializers.CharField(max_length=100)
    question4 = serializers.CharField(max_length=100)
    question5 = serializers.CharField(max_length=100)
    question6 = serializers.CharField(max_length=100)
    question7 = serializers.CharField(max_length=100)
    question8 = serializers.CharField(max_length=100)
    question9 = serializers.CharField(max_length=100)
    question10 = serializers.CharField(max_length=100)
    question11 = serializers.CharField(max_length=100)
    question12 = serializers.CharField(max_length=100)
    question13 = serializers.CharField(max_length=100)
    question14 = serializers.CharField(max_length=100)
    question15 = serializers.CharField(max_length=100)
    question16 = serializers.CharField(max_length=100)
    question17 = serializers.CharField(max_length=100)
    question18 = serializers.CharField(max_length=100)
    question19 = serializers.CharField(max_length=100)

# class SignUpSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = UserModel
#         # fields = ["name","age","email","password"]
#         fields = '__all__'

# class SignInSerializer(serializers.Serializer):
#     email = serializers.EmailField()
#     password = serializers.CharField(write_only=True)

class UserSerializer(serializers.Serializer):
    class Meta:
        model = User
        name = serializers.CharField(read_only=True)

class SignUpSerializer(serializers.ModelSerializer):
    age = serializers.IntegerField(write_only=True)
    resume = serializers.FileField(write_only=True, required=False)  # Added resume field, optional

    class Meta:
        model = User
        fields = ["username", "email", "password", "age", "resume"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        age = validated_data.pop("age")
        resume = validated_data.pop("resume", None)  # Extract resume if provided
        user = User.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"]
        )
        profile = UserProfile.objects.create(user=user, age=age)
        if resume:
            profile.resume = resume
            profile.save()
        return user

class SignInSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)