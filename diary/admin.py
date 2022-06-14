from django.contrib import admin

from diary.models import Diary, DiaryFileLog, DiaryPostLog

# Register your models here.

# 관리자 사이트에서 컨트롤 할 수 있도록 해당하는 모델들을 추가시킴
admin.site.register(Diary)
admin.site.register(DiaryFileLog)
admin.site.register(DiaryPostLog)