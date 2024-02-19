from rest_framework import serializers
from .models import User, Payment
from courses.serializers import CourseSerializer, LessonSerializer


class UserProfileSerializer(serializers.ModelSerializer):
    payment_history = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'phone', 'city', 'avatar', 'payment_history']


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'
