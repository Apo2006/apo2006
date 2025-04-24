from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings  # импортируем settings для ForeignKey

class CustomUser(AbstractUser):
    # Пока оставим пустым, но сюда можно добавить дополнительные поля, например телефон
    pass

class Address(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='addresses')
    full_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    address_line = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    country = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.full_name}, {self.address_line}, {self.city}"
