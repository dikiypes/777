from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from courses.models import Course, Lesson


class Payment(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    payment_date = models.DateField()
    paid_course = models.ForeignKey(Course, null=True, blank=True, on_delete=models.CASCADE)
    paid_lesson = models.ForeignKey(Lesson, null=True, blank=True, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=20, choices=[('cash', 'Cash'), ('transfer', 'Transfer')])


class User(AbstractUser):
    username = None
    groups = models.ManyToManyField(Group, related_name='custom_user_set')
    user_permissions = models.ManyToManyField(Permission, related_name='custom_user_set_permissions')
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    city = models.CharField(max_length=255)
    avatar = models.ImageField(upload_to='avatars/')
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
