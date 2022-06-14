from django.conf import settings
from django.contrib.auth.hashers import check_password, make_password
from rest_framework.response import Response
from rest_framework import status, viewsets

from .serializers import AuthLogSerializer, LoginPlatformSerializer, UserSerializer
from .utils import get_tokens_for_user
from .models import AuthLog, User, UserLoginPlatform

# 로그인 할때 사용하는 뷰셋입니다.
class UserAuthViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, request, format=None):
        data = {
            "ok": True
        }
        return Response(data, status=status.HTTP_200_OK)
    
    def register(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            obj = {
                "success": True,
                "message": "성공적으로 가입되었습니다!"
            }
            return Response(obj, status=status.HTTP_201_CREATED)
        obj = {
            "success": False,
            "message": serializer.errors,
        }
        return Response(obj, status=status.HTTP_400_BAD_REQUEST)
    
    def login(self, request, format=None):
        queryset = User.objects.get(id=request.data['id'])
        if(check_password(request.data['password'], queryset.password)):
            token = get_tokens_for_user(queryset)
            token['expires_in'] = settings.SIMPLE_JWT['ACCESS_TOKEN_LIFETIME']

            obj = {
                "success": True,
                "data": token,
            }
            return Response(obj, status=status.HTTP_200_OK)
        
        obj = {
            "sucess": False,
            "message": "비밀번호가 올바르지 않습니다!"
        }
        return Response(obj, status=status.HTTP_401_UNAUTHORIZED)

# 유저를 추가, 검색할때 사용하는 뷰셋입니다.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# 로그인 로그를 기록하는 뷰셋입니다.
class AuthLogViewSet(viewsets.ModelViewSet):
    queryset = AuthLog.objects.all()
    serializer_class = AuthLogSerializer

# 로그인한 플랫폼을 기록하는 뷰셋입니다.
class LoginPlatformViewSet(viewsets.ModelViewSet):
    queryset = UserLoginPlatform.objects.all()
    serializer_class = LoginPlatformSerializer