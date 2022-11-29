from django.db import models
import uuid

# Create your models here.
class Cnab(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4, editable=False, unique=True, primary_key=True
    )
    tipo = models.IntegerField()
    data = models.DateField()
    valor = models.FloatField()
    cartao = models.CharField(max_length=12)
    cpf = models.CharField(max_length=11)
    hora = models.TimeField()
    dono = models.ForeignKey(
        "donos_loja.Dono_loja", related_name="cnab", on_delete=models.CASCADE
    )
