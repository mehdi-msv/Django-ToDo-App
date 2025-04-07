from rest_framework_simplejwt.serializers import TokenObtainPairSerializer



class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    '''
    This serializer returns a JSON Web Token that includes the user's email and id.
    '''
    def validate(self, attrs):
        validated_data = super().validate(attrs)
        validated_data['user'] = self.user.username
        validated_data['user_id'] = self.user.id
        return validated_data