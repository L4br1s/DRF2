from rest_framework import serializers
from Apps.clientes.models import Cliente
from Apps.clientes.validators import validate_cpf,validate_rg,validate_nome,validate_celular

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'
    def validate(self,data):
        if not validate_cpf(data['cpf']):
            raise serializers.ValidationError({'cpf':"CPF INVÁLIDO!!!"})
        if not validate_nome(data['nome']):
            raise serializers.ValidationError({'nome':"NOME INVÁLIDO, DEVE CONTER APENAS LETRAS"})
        if not validate_rg(data['rg']):
            raise serializers.ValidationError({'rg':"RG DEVE CONTER 9 DIGÍTOS"})
        if not validate_celular(data['celular']):
            raise serializers.ValidationError({'celular':'NUMERO DE CELULAR INVÁLIDO'})

        return data




