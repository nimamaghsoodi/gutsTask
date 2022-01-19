from rest_framework import serializers
from .models import EP_ENGINE_USAGE

class UsageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EP_ENGINE_USAGE
        fields = ('id','POD_NAME', 'CPU_USAGE','RAM_USAGE','TIME_STAMP')