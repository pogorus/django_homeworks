from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.serializers import ValidationError

from advertisements.models import Advertisement


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name',
                  'last_name',)


class AdvertisementSerializer(serializers.ModelSerializer):

    creator = UserSerializer(
        read_only=True,
    )

    class Meta:
        model = Advertisement
        fields = ('id', 'title', 'description', 'creator',
                  'status', 'created_at', )

    def create(self, validated_data):

        validated_data["creator"] = self.context["request"].user
        return super().create(validated_data)

    def validate(self, data):

        open_advs = Advertisement.objects.filter(creator=self.context['request'].user, status='OPEN')
        if len(open_advs) >= 10 and data['status'] == 'OPEN':
            raise ValidationError('Maximum open advertisements is 10')

        return data
