# serializers.py

from rest_framework import serializers

from django.contrib.auth.hashers import make_password
from .models import User, Producto_maquina, Producto, Maquina, Reporte, Sugerencias, Formatos, Resinas, Actividad

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','email', 'nombre', 'username','no_empleado','apellido_paterno','apellido_materno', 'rol', 'password', 'is_active', 'is_staff', 'profile_picture']
        extra_kwargs = {'password': {'write_only': True}}

    def update(self, instance, validated_data):
        password = validated_data.get('password', None)
        if password:
            instance.set_password(password)  
            validated_data.pop('password')
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        
        instance.save()
        return instance
    
    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)
    
class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto  
        fields = ['id', 'producto', 'descripcion', 'codigo_cliente', 'resina_1', 'categoria', 'estado']
        
class MaquinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Maquina
        fields = ['id', 'maquina', 'estado', 'Formato', 'planta']
        
        
class ProductoMaquinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto_maquina
        fields = ['id', 'Ruta', 'Descripcion_1', 'Categoria', 'Operación', 'Subcontratacion', 'Centro_trabajo_ppal', 'Destino_ope', 'Cod_maquina',
                  'Tipo_tpo_operacional', 'Tiempo_ajuste', 'Tpo_operacional', 'Cadencia',
                  'Cadence_theo', 'Utillaje', 'Eficiencia',
                  'Formato']
        
class ReporteSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True) 
    producto = ProductoSerializer(read_only=True)
    maquina = MaquinaSerializer(read_only=True)
    producto_maquina = ProductoMaquinaSerializer(read_only=True)
    
    producto_id = serializers.PrimaryKeyRelatedField(
        queryset=Producto.objects.all(), write_only=True, source='producto'
    )
    producto_maquina_id = serializers.PrimaryKeyRelatedField(
        queryset=Producto_maquina.objects.all(), write_only=True, source='producto_maquina'
    )
    maquina_id = serializers.PrimaryKeyRelatedField(
        queryset=Maquina.objects.all(), write_only=True, source='maquina'
    )
    class Meta:
        model = Reporte
        fields = ['id','user','producto','producto_id', 'producto_maquina','maquina','maquina_id','producto_maquina_id','is_active','ruta', 'content','fecha', 'comentario']
        read_only_fields = ['fecha', 'user']
        
        
class SendEmailSerializer(serializers.Serializer):
    email = serializers.EmailField()

class VerifyCodeSerializer(serializers.Serializer):
    email = serializers.EmailField()
    code = serializers.CharField(max_length=100)

class ResetPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()
    code = serializers.CharField(max_length=100)
    new_password = serializers.CharField(write_only=True)


class ResetPasswordResponseSerializer(serializers.Serializer):
    success = serializers.BooleanField()
    message = serializers.CharField()
    
class SugerenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sugerencias
        fields = ['id', 'user_id', 'sugerencia', 'fecha', 'is_active']
        
class FormatoSerializer(serializers.ModelSerializer):
    class Meta:
        model= Formatos
        fiels = ['id', 'formato']
        
class ResinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resinas
        fields = ['id','codigo_interno', 'resina', 'densidad_de_bulto', 'temperatura_secado', 'tiempo_secado', 'densidad']
        
class ActividadSerializer(serializers.ModelSerializer):
    usuario= UserSerializer(read_only=True)
    class Meta:
        model = Actividad
        fields = ['id', 'usuario_id', 'usuario','actividad', 'metodo', 'fecha']
        