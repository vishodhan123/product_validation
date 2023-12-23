from django.db import models

# Create your models here.

from django.db import models
import uuid


class Product(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    status = models.CharField(max_length=10)  # 'active' or 'inactive'
