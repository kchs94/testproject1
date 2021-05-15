
from django.contrib import admin
from django.urls import path, include  # urls 간 연결해주는 함수
from loginapp import views  # 모델 가져오기

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.login),
    path('users/', views.user_list),
    path('users/<int:pk>', views.user),
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    # path('createEvent/',)
]
