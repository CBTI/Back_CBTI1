from django.db import models

# Create your models here.
class CBTIapp2_model(models.Model):
    username = models.CharField(max_length = 32, verbose_name = '사용자명')
    useremail = models.EmailField(max_length = 32, verbose_name = '사용자이메일')
    password = models.CharField(max_length = 32, verbose_name = '비밀번호')
    register_datetime = models.DateField(auto_now_add = True, verbose_name = "가입날짜")
    # 모델 안에 데이터가 문자열로 변환이 될 때 어떻게 나올지(반환할지) 정의하는 파이썬의 함수 __str__ 
    # 파이썬은 특정 객체(클래스)를 문자열로 호출할떄 __str__ 함수가 실행되도록 되어있음, 
    # 아래 __str__함수 만들지 않으면 회원을 추가 하면 '클래스명 object'로 보임.
    # 이 방법 외에 사용자명과 비밀번호를 한 화면에 보고싶으면 admin.py의 주석 참고
    def __str__(self):
        return self.username
    
    
    class Meta:
        # 별도의 테이블명을 지정하고 싶을때
        #db_table = 'user_define_table'# 안에 이름 넣으면 끝
        verbose_name = '사용자 모임'# 장고가 자동으로 's'붙여줌
        verbose_name_plural = '사용자 모임'
'''
        위 작성후 콘솔에서 프로젝트 폴더 위치에서 python .\manage.py makemigrations 명령어 치면
        
        Migrations for 'CBTIapp2':
          CBTIapp2\migrations\0001_initial.py
            - Create model CBTIapp2_model
        
        라고 출력된다.
        이러면 migrations 폴더 안에 db를 어떻게 만들어야할지 models.py(현재 이 파일)을 참조해서 만들어진 
        CBTIapp2/migrations/0001_initial.py 에 적혀있다.
        
        이후 python manage.py migrate
        
        위 내용 수정할때도 수정 후 python .\manage.py makemigrations 하면 Alter 명령구가 나온다.
        
        # Sqlite3
        콘솔 프로젝트 폴더 에서 .\sqlite3.exe .\db.sqlite3
        
        현재 테이블들 확인      =>   .tables
        특정 테이븡 스키마 확인 =>   .schema 위에서찾은테이블이름
        
        sqlite를 나가려면  => .q
'''
    