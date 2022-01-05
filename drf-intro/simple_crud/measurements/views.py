from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from rest_framework.generics import ListCreateAPIView, CreateAPIView, RetrieveUpdateAPIView
from rest_framework.response import Response

from .models import Sensor, Measurement
from .serializers import SensorSerializer, MeasurementSerializer, SensorDetailSerializer


class SensorView(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class SingleSensorView(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer


class MeasurementView(CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer
