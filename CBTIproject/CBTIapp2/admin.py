from django.contrib import admin
from .models import CBTIapp2_model
# Register your models here.

class CBTIapp2_model_Admin(admin.ModelAdmin):
    #  models.py 에서 __str__를 쓰지 않고, 하ㅓㄴ화면에 사용자명 - 비밀번호 화면으로 보고싶은 경우
    
    list_display = ('username', 'password', 'useremail')#이 줄을 주석 해제하고, pass를 주석처리
    
    pass


admin.site.register(CBTIapp2_model, CBTIapp2_model_Admin)