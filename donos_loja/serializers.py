from rest_framework import serializers
from .models import Dono_loja
from CNAB.serializers import CNABSerializer


class DonoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dono_loja
        fields = [
            "id",
            "dono_da_loja",
            "nome_da_loja",
            "cnab",
        ]
        read_only_fields = ["cnab"]

    def create(self, validated_data):
        dono, _ = Dono_loja.objects.get_or_create(**validated_data)
        return dono
