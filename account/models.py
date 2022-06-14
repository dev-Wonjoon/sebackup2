from django.db import models
from django.contrib.auth.models import AbstractUser

'''
유저를 표현하는 모델입니다. django에서 모델은 데이터베이스 역할을 합니다.
AbstractUser가 인자로 들어오는 것은 django에서 지원하는 유저 모델을 가져와서
덧붙여서 사용하기 때문입니다. SQL로 변환시
CREATE TABLE User (
    user_seq INT AUTO_INCREMENT PRIMARY KEY NOT NULL, --django에선 AutoField라고 Auto_INCREMENT 역할을 하는 필드가 존재 (아무런 PK를 설정하지 않을시 AutoField를 PK로 지정함)
    id VARCHAR(32) UNIQUE NOT NULL, --EmailField는 django에서 지원하는 필드로 sql에서 varchar로 대체
    password VARCHAR(512) NOT NULL, --512로 들어오는 것은 비밀번호를 해쉬로 받기 위함
    nickname VARCHAR(24) NOT NULL
) '''
class User(AbstractUser):
    user_seq = models.AutoField(primary_key=True)
    id = models.EmailField(max_length=32, unique=True)
    password = models.CharField(max_length=512)
    nickname = models.CharField(max_length=24)



'''
유저 계정을 기록하는 테이블입니다. 계정에 변경사항이 있을때 변동됩니다.
CREATED TABLE AuthLog (
    auth_seq INT AUTO_INCEMENT PRIMARY KEY NOT NULL,
    auth_registed DATE NOT NULL,
    auth_updated DATE NOT NULL,
    auth_after VARCHAR(24) NOT NULL,
    auth_user_pk INT NOT NULL,
    FOREIGE KEY (`auth_user_pk`)
    REFERENCES `User` (`user_seq`) ON DELETE NO ACTION
) '''
class AuthLog(models.Model):
    auth_seq = models.AutoField(primary_key=True)
    auth_registed = models.DateTimeField(auto_now_add=True)
    auth_updated = models.DateTimeField(auto_now=True)
    auth_after = models.CharField(max_length=24)
    auth_user_pk = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='AuthLogToUser')



'''
유저가 로그인한 플랫폼을 기록하는 테이블입니다.
CREATE TABLE UserLoginPlatform (
    ull_seq INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    ull_platform VARCHAR(16) NOT NULL,
    ull_last_login DATE NOT NULL,
    ull_user_pk INT NOT NULL,
    FOREIGE KEY (`ull_user_pk`)
    REFERENCES `User` (`user_seq`)
)
'''
class UserLoginPlatform(models.Model):
    ull_seq = models.AutoField(primary_key=True)
    ull_platform = models.CharField(max_length=16)
    ull_last_login = models.DateTimeField(auto_now_add=True)
    ull_user_pk = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='PlatformToUser')