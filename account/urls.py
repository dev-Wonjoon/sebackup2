from django.db import router
from django.urls import path, include
from .views import AuthLogViewSet, LoginPlatformViewSet, UserAuthViewSet, UserViewSet
from rest_framework.routers import DefaultRouter


'''
views.py에서 함수로 기능을 나눈 view를 매핑합니다.
'''
login = UserAuthViewSet.as_view({
    'post': 'login',
})

registe = UserAuthViewSet.as_view({
    'post': 'register'
})

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='users')
router.register(r'authlogs', AuthLogViewSet, basename='authlogs')
router.register(r'platformlogs', LoginPlatformViewSet, basename='platformlogs')


urlpatterns = [
    path('login/', login, name='login'), #해당하는 urls에 post시 login 함수로 매핑합니다.
    path('registe/', registe, name='registe'), # 해당하는 urls에 post시 register 함수로 매핑합니다.
    path('', include(router.urls)), # router 기능으로 url들을 묶고 url을 매핑합니다
]