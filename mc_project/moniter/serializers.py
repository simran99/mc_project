from user.models import emergency
from rest_framework import serializers

class EmergencySerializer(serializers.ModelSerializer):
    class Meta:
        model = emergency
        fields = ['pid', 'state','timestamp']