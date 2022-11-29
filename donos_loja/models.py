from django.db import models
import uuid

# Create your models here.
class Dono_loja(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4, editable=False, unique=True, primary_key=True
    )
    dono_da_loja = models.CharField(max_length=20)
    nome_da_loja = models.CharField(max_length=20)
