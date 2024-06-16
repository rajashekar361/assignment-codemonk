from rest_framework import serializers
from Authentication.models import Details


class SignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Details
        fields = ['Name', 'Email', 'Pwd', 'dob', 'createdAt', 'modifiedAt']
