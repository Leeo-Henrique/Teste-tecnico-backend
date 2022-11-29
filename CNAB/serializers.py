from rest_framework import serializers
from .models import Cnab


class CNABSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cnab
        fields = [
            "id",
            "tipo",
            "data",
            "valor",
            "cartao",
            "cpf",
            "hora",
            "dono",
        ]
        read_only_fields = ["id"]

    data = serializers.DateTimeField(format="%Y-%m-%d")

    def create(self, validated_data):
        cnab, _ = Cnab.objects.get_or_create(**validated_data)
        return cnab
