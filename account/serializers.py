from .models import AuthLog, User, UserLoginPlatform
from rest_framework import serializers
from django.contrib.auth.hashers import make_password

'''
views.py에 요청이 들어오면 해당하는 시리얼라이저로 데이터를 넣습니다.
Json -> OrderedDict -> Queryset -> DB 순서로 변환시킵니다. 
유저 시리얼라이저입니다.
내부 Meta 클래스는 다른 데이터(모델)에 대한 정보를 제공하는 클래스입니다.
'''
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('seq', 'id', 'password', 'nickname')

        # 추가 요구사항 비밀번호 최소 4자리 이상, 쓰기 전용
        extra_kwargs = {
            'password': {
                'write_only': True,
                'required': True,
                'min_length': 4
            }
        }

    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(user.password)
        user.save()
        user.password = None
        return User

# AuthLog 모델을 사용하는 시리얼라이저입니다.
class AuthLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthLog
        fields = ('auth_seq', 'auth_registed', 'auth_updated', 'auth_after', 'auth_user_pk')

# UserLoginPlatform 모델을 사용하는 시리얼라이저입니다.
class LoginPlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserLoginPlatform
        fields = ('ull_seq', 'ull_platform', 'ull_last_login', 'ull_user_pk')