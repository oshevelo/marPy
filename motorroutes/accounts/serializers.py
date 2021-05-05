from rest_framework import serializers
from .models import UserProfile

class ValidationMixIn():
    def validate_userprofile(self, data):
        u_count = UserProfile.objects.filter(id=data.get('id')).count()
        if u_count == 1:
            return data
        else:
            raise serializers.ValidationError("wrong UserProfile id")

class UserProfileNestedSerializer(serializers.ModelSerializer,ValidationMixIn):
    id = serializers.IntegerField()
    date_of_birth = serializers.DateField(read_only=True)
    phone_number = serializers.CharField(read_only=True)
    bio = serializers.CharField(read_only=True)
    gender = serializers.CharField(read_only=True)

    class Meta:
        model = UserProfile
        fields = ['id', 'date_of_birth', 'phone_number', 'gender', 'bio']
