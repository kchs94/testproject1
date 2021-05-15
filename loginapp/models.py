from django.db import models

# Create your models here.


# 사용자 모델
class User(models.Model):
    name = models.CharField(max_length=6)           # 이름
    email = models.CharField(max_length=200)        # 이메일
    password = models.CharField(max_length=200)     # 암호화 하면 문자가 길어지기에
    create_date = models.DateTimeField(auto_now_add=True)            # 생성일


# # 게시판 모델
# class Board(models.Model):
#     id = models.ForeignKey(User, on_delete=models.CASCADE)# 각 유저 마다 외래키
#     object = models.CharField(max_length=200)             # 객체 이름
#     video = models.CharField(max_length=200)              # 비디오
#     thumbNail = models.ImageField()                       # 썸네일
#     dateTime = models.DateTimeField(auto_now_add=True)    # 생성일


