from rest_framework import serializers  # 시리얼라이저 가져오기
from .models import User


# User 모델로 만든 데이터를 json 형태로 바꿔준다.
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'password']  # id는 pk로 쓰이는 자동 생성 필드
