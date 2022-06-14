from django.contrib import admin

from account.models import User, AuthLog, UserLoginPlatform

# 관리자 사이트에서 컨트롤 할 수 있도록 해당하는 모델들을 추가시킴
admin.site.register(User)
admin.site.register(AuthLog)
admin.site.register(UserLoginPlatform)