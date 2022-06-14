from django.urls import path
from diary.views import DiaryViewSet, PostViewSet, FileLogViewSet
'''
다이어리 관련 url 매핑입니다.
각각 맞는 뷰셋에 url을 매핑합니다.
'''

urlpatterns = [
    path('diarys', DiaryViewSet.as_view()),
    path('postlogs', PostViewSet.as_view()),
    path('filelogs', FileLogViewSet.as_view()),
]