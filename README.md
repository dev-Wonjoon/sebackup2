# 해당하는 README는 프로젝트를 설명하기 위해 사용합니다.
> 파이썬 3.6 이상 필요합니다.
> 주석이 있는 파일은 account, diary 디렉토리의 models.py, serializers.py, views.py, urls.py 입니다.
> 나머지 파일들은 서버를 실행시키기 위한 django의 보조 파일들입니다. (자동 생성)

---------------------------------------------

## 파일 설명
> models.py // 데이터베이스 모델을 정의해둔 파일입니다.
> serializers.py // json타입을 데이터베이스 쿼리셋으로 변환시켜주는 역할을 합니다.
> views.py //서버에서 요청이 들어오면 처리를 하는 부분입니다.
> urls.py // views파일의 내용을 라우팅 해주는 파일입니다.

---------------------------------------------
## 필요한 패키지
> pip install django djangorestframework authentication

---------------------------------------------
## migrate 관련 알림
> 프로젝트 파일에 manage.py 파일이 있는 위치로 이동 후
> python ./manage.py makemigrations
> python ./manage.py migrate

---------------------------------------------
## 서버 실행
> python ./manage.py runserver
> 접속은 127.0.0.1:8000

---------------------------------------------
## 데이터를 추가하고 삭제하기
> python ./manage.py createsuperuser
> 데이터 입력 후 127.0.0.1:8000/admin 접속
> 미리 생성해둔 관리자 계정은 id : admin / password : 1234