from rest_framework import serializers
from .models import Diary, DiaryFileLog, DiaryPostLog


'''
다이어리 시리얼라이저 입니다.
Meta 클래스는 다른 데이터(모델)에 대한 정보를 제공하는 클래스입니다.
'''
class DiarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Diary
        fields = ('diary_seq', 'diary_title', 'diary_content', 'diary_user_pk')

# 다이어리 작성을 기록하는 시리얼라이저입니다.
class PostLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiaryPostLog
        fields = ('dp_seq', 'dp_created', 'dp_updated', 'dp_diary_pk')

# 다이어리에 업로드한 파일을 기록하는 시리얼라이저입니다.
class FileLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiaryFileLog
        fields = ('df_seq', 'df_filepath', 'df_filename', 'df_upload_date', 'df_diary_pk')
