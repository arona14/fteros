from rest_framework import serializers
from util.models import ConnectionSetting,FeedBack

class ConnectionSettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConnectionSetting
        fields = '__all__'


class FeedBackSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedBack
        fields = '__all__'