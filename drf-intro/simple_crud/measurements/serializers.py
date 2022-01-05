from rest_framework import serializers
from .models import Sensor, Measurement


class SensorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description']


class MeasurementSerializer(serializers.ModelSerializer):

    class Meta:
        model = Measurement
        fields = ['sensor', 'value', 'created_at']


class SensorDetailSerializer(serializers.ModelSerializer):
    measurements = MeasurementSerializer(required=False, read_only=True, many=True)

    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'measurements']