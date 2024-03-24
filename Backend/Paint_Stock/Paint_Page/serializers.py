from rest_framework import serializers
from .models import Paints, PaintUser

class PaintsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paints
        fields = ['id', 'colour', 'stock_level']

class PaintUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaintUser
        fields = ['id', 'username', 'is_admin', 'is_editor']