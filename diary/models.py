from django.db import models
from account.models import User

'''
다이어리 모델입니다. SQL로 변환 시 (mysql)
CREATE TABLE Diary (
    diary_seq INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    diary_title VARCHAR(64) NOT NULL,
    diary_content TEXT(65536) NOT NULL,
    diary_img BLOB NOT NULL, --장고에선 이미지필드가 따로 있지만 mysql에선 적절한 데이터타입을 찾을 수가 없어서 BLOB으로 대체
    diary_user_pk INT NOT NULL,
    FOREIGN KEY (`diary_user_pk`)
    REFERENCES `User` (`user_seq`)
) '''
class Diary(models.Model):
    diary_seq = models.AutoField(primary_key=True)
    diary_title = models.CharField(max_length=64)
    diary_content = models.TextField(max_length=65536)
    diary_img = models.ImageField()
    diary_user_pk = models.ForeignKey(User, on_delete=models.DO_NOTHING)



'''
다이어리 작성을 기록하는 테이블입니다.
CREATE TABLE DiaryPostLog (
    dp_seq INT AUTO_INCREMENT PRIMARY KEY,
    dp_created DATE NOT NULL,
    dp_updated DATE NOT NULL,
    dp_diary_pk INT NOT NULL,
    FOREIGE KEY (`dp_seq`)
    REFERENCES `Diary` (`diary_seq`)
) '''
class DiaryPostLog(models.Model):
    dp_seq = models.AutoField(primary_key=True)
    dp_created = models.DateTimeField(auto_now_add=True)
    dp_updated = models.DateTimeField(auto_now=True)
    dp_diary_pk = models.ForeignKey(Diary, on_delete=models.DO_NOTHING)



'''
다이어리에 업로드한 파일을 기록하는 테이블입니다.
CREATE TABLE DiaryFileLog (
    df_seq INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    df_filepath VARCHAR(256) NOT NULL,
    df_filename VARCHAR(64) NOT NULL,
    df_upload_date DATE NOT NULL,
    df_diary_pk INT NOT NULL,
    FOREIGE KEY (`df_diary_pk`)
    REFERENCES `Diary` (`diary_seq`)
)
'''
class DiaryFileLog(models.Model):
    df_seq = models.AutoField(primary_key=True)
    df_filepath = models.CharField(max_length=256)
    df_filename = models.CharField(max_length=64)
    df_upload_date = models.DateTimeField(auto_now_add=True)
    df_diary_pk = models.ForeignKey(Diary, on_delete=models.DO_NOTHING)