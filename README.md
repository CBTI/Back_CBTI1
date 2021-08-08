# Back_CBTI

CBTI Backend API 

## 회원가입 관련

- ✅ 회원가입) [POST] {host}/CBTIapp2/user/register 
```json
요청 데이터 형식 
{
  "id":"id1234",
  "password":"pw1234",
  "name":"이름",
  "nickname":"파댕이",
  "phone":"010-1234-1234",
  "address":"서울 어딘가"
}
```
```json
응답 데이터 형식 
{
  "rtnCode":"200",
  "rtnMsg":"회원가입 완료"
}

또는

{
  "rtnCode":"500",
  "rtnMsg":"회원가입 실패"
}
```

- ✅ 로그인) [POST] {host}/CBTIapp2/user/login 
```json
요청 데이터 형식 
{
  "id":"id1234",
  "password":"pw1234"
}
```
```json
응답 데이터 형식 
{
  "rtnCode":"200",
  "rtnMsg":"로그인 성공"
}

또는

{
  "rtnCode":"500",
  "rtnMsg":"패스워드가 일치하지 않습니다"
}
```

- ✅ 아이디 중복 체크) [POST] {host}/CBTIapp2/user/idCheck 
```json
요청 데이터 형식 
{
  "id":"id1234"
}
```
```json
응답 데이터 형식 
{
  "rtnCode":"200",
  "rtnMsg":"가입 가능한 ID"
}

또는

{
  "rtnCode":"502",
  "rtnMsg":"이미 존재하는 아이디입니다"
}
```

- ✅ 닉네임 중복 체크) [POST] {host}/CBTIapp2/user/nickCheck
```json
요청 데이터 형식 
{
  "nickname":"닉네임1234"
}
```
```json
응답 데이터 형식 
{
  "rtnCode":"200",
  "rtnMsg":"사용가능한 닉네임입니다"
}

또는

{
  "rtnCode":"502",
  "rtnMsg":"이미 존재하는 닉네임입니다"
}
```
