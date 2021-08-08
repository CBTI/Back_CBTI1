from django.shortcuts import render
from .models import CBTIapp2_model
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.hashers import make_password  # 비밀번호 암호화저장(register)
from django.contrib.auth.hashers import check_password  # 비밀번호 검사(login)
from django.shortcuts import redirect  # View의 Redirect , user for login return redirect('사이트명')
from django.views.decorators.csrf import csrf_exempt
import mysql.connector
import json

# MariaDB connection
config = {
    "user": "cbti",
    "password": "cbti1234",
    "host": "127.0.0.1",  # local
    "database": "cbti",  # Database name
    "port": 3307  # port는 최초 설치 시 입력한 값(기본값은 3306)
}

conn = mysql.connector.connect(**config)
conn.autocommit = True
c = conn.cursor()


# Create your views here.
@csrf_exempt
def register(request):
    if request.method == "GET":
        return render(request, 'register.html')

    elif request.method == "POST":
        # 회원가입 처리
        data = json.loads(request.body)
        id = data['id']
        password = make_password(data['password'])
        name = data['name']
        nickname = data['nickname']
        phone = data['phone']
        address = data['address']
        group = 'user'
        query = f'INSERT INTO tb_cbti_user VALUES(\'{id}\', \'{password}\', \'{name}\', \'{nickname}\', \'{phone}\', \'{address}\', \'{group}\')'

        # 위와 아래의 차이는, 위는 username이나 pasword 입력하지 않아도 제출 버튼이 눌러져서 해당 코드에 key값이 없다는 에러 발생, get메소드를 통해 해당 에러 해결

        # username = request.POST.get('username', None)
        # useremail = request.POST.get('useremail', None)
        # password = request.POST.get('password', None)
        # re_password = request.POST.get('re-password', None)

        '''
        # 비밀번호가 다르면 메시지와함께 리턴 , 너무단순하니까 백엔드에서 데이터를 프론트로 전달해서 메시지 출력하도록 변경
        if password != re_password:
            return HttpResponse("비밀번호가 다름")
        '''

        # if not (username and password and re_password):  # None은 False로 인식됨.
        #     res_data['error'] = "모든 부분을 입력하셔야 합니다."
        #
        # # 다르면 리턴
        # elif password != re_password:
        #     res_data['error'] = "입력하신 2개의 비밀번호가 서로 다릅니다.."
        # # 같으면 저장
        # else:
        #     # 인스턴스 생성
        #     cbtiapp2_model = CBTIapp2_model(
        #         username=username,
        #         useremail=useremail,
        #         password=make_password(password),
        #     )
        #
        #     # 저장
        #     cbtiapp2_model.save()

        # '''
        # # 인스턴스 생성
        # cbtiapp2_model = CBTIapp2_model(
        #     username = username,
        #     password = password,
        # )
        # # 저장
        # cbtiapp2_model.save()
        # '''
        # 데이터 삽입
        try:
            c.execute(query)
            res_data = {'rtnCode': '200', 'rtnMsg': '회원가입 완료'}
        except:
            res_data = {'rtnCode': '500', 'rtnMsg': '회원가입 실패'}  # 응답 데이터
        # return render(request, 'register.html', res_data)
        return JsonResponse(res_data)


@csrf_exempt
def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')

    elif request.method == 'POST':
        data = json.loads(request.body)
        id = data['id']
        password = data['password']
        res_data = {}
        # 기존 db의 모델과 같은 값을 가져온다.
        query = f'SELECT PASSWORD FROM TB_CBTI_USER WHERE ID = \'{id}\''
        try:
            c.execute(query)
            # password가 맞는지 확인
            if check_password(password, c.fetchone()[0]):
                res_data['rtnCode'] = 200
                res_data['rtnMsg'] = '로그인 성공'
            else:
                res_data['rtnCode'] = 501
                res_data['rtnMsg'] = '패스워드가 일치하지 않습니다'
        except:
            res_data['rtnCode'] = 500
            res_data['rtnMsg'] = '기타 오류'
        return JsonResponse(res_data)


@csrf_exempt
def id_check(request):
    if request.method == 'GET':
        print('nothing')
    elif request.method == 'POST':
        data = json.loads(request.body)
        id = data['id']
        res_data = {}
        query = f'SELECT * FROM TB_CBTI_USER WHERE ID = \'{id}\''
        try:
            c.execute(query)
            sql_data = c.fetchall()
            if len(sql_data) == 0:
                res_data['rtnCode'] = 200
                res_data['rtnMsg'] = '가입 가능한 ID'
            else:
                res_data['rtnCode'] = 502
                res_data['rtnMsg'] = '이미 존재하는 아이디입니다'
        except:
            res_data['rtnCode'] = 500
            res_data['rtnMsg'] = '기타 오류'
        return JsonResponse(res_data)


@csrf_exempt
def nickname_check(request):
    if request.method == 'GET':
        print('nothing')
    elif request.method == 'POST':
        data = json.loads(request.body)
        nickname = data['nickname']
        res_data = {}
        query = f'SELECT * FROM TB_CBTI_USER WHERE NICKNAME = \'{nickname}\''
        try:
            c.execute(query)
            sql_data = c.fetchall()
            if len(sql_data) == 0:
                res_data['rtnCode'] = 200
                res_data['rtnMsg'] = '사용가능한 닉네임입니다'
            else:
                res_data['rtnCode'] = 502
                res_data['rtnMsg'] = '이미 존재하는 닉네임입니다'
        except:
            res_data['rtnCode'] = 500
            res_data['rtnMsg'] = '기타 오류'
        return JsonResponse(res_data)


def home(request):
    user_pk = request.session.get('user')

    if user_pk:
        cbtiapp2_model = CBTIapp2_model.objects.get(pk=user_pk)
        return HttpResponse(cbtiapp2_model.username)

    return HttpResponse("로그인 성공")
