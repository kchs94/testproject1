from django.db import models

# Create your models here.


# 사용자 모델
class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)                            # 이름
    email = models.CharField(max_length=200)                         # 이메일
    password = models.CharField(max_length=200)                      # 암호화 하면 문자가 길어지기에
    create_date = models.DateTimeField(auto_now_add=True)            # 생성일


# 게시판 모델
class Video(models.Model):
    user_id = models.ForeignKey(User, related_name="user", on_delete=models.CASCADE, db_column="user_id")  # 외래키
    id = models.AutoField(primary_key=True)               # 비디오 id
    object = models.CharField(max_length=200)             # 객체 이름
    video = models.CharField(max_length=200)              # 비디오
    thumbNail = models.CharField(max_length=200)          # 썸네일
    dateTime = models.DateTimeField(null=True)            # 생성일


