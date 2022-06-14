from multiprocessing.sharedctypes import Value
from django.shortcuts import render
from itsdangerous import Serializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from diary.models import Diary, DiaryFileLog, DiaryPostLog
from diary.serializers import DiarySerializer, FileLogSerializer, PostLogSerializer


'''
다이어리 뷰셋입니다. 
get 요청이 들어올 경우 해당하는 요청의 유저 pk를 따와서 다이어리를 검색합니다.
post 요청이 들어올 경우 is_valid 함수에서 들어온 값이 유효한지 검사한 후 데이터베이스에 데이터를 저장합니다.
'''
class DiaryViewSet(APIView):
    def get(self, request, format=None):
        diarys = Diary.objects.get(diary_pk=request.data['user_seq'])
        serializer = DiarySerializer(diarys)
        return Response(serializer.data)
    
    def post(self,request, format=None):
        serializer = DiarySerializer(data=request.data)
        if serializer.is_valid(raise_exception=ValueError):
            serializer.create(validated_data=request.data)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(status=status.HTTP_400_BAD_REQUEST)

# 다이어리를 작성했을때 로그를 작성하는 뷰셋입니다.
class PostViewSet(APIView):
    def get(self, request, format=None):
        postlog = DiaryPostLog.objects.all()
        serializer = DiaryPostLog(postlog, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = PostLogSerializer(data=request.data)
        if serializer.is_valid(raise_exception=ValueError):
            serializer.create(validated_data=request.data)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(status=status.HTTP_400_BAD_REQUEST)

# 파일 업로드 로그를 작성하는 뷰셋입니다.
class FileLogViewSet(APIView):
    
    def get(self, request, format=None):
        filelog = DiaryFileLog.objects.all()
        serialzier = FileLogSerializer(filelog, many=True)
        return Response(serialzier.data)
    
    def post(self, request, format=None):
        serializer = FileLogSerializer(data=request.data)
        if serializer.is_valid(raise_exception=ValueError):
            serializer.create(validated_data=request.data)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(status=status.HTTP_400_BAD_REQUEST)