from django.contrib.auth.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
class EmailOrUsernameTokenSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        identity = attrs.get(self.username_field, '')
        if identity and '@' in identity:
            user = User.objects.filter(email__iexact=identity).first()
            if user:
                attrs[self.username_field] = user.get_username()
        return super().validate(attrs)
class EmailOrUsernameTokenView(TokenObtainPairView):
    serializer_class = EmailOrUsernameTokenSerializer
