"""Django8 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from vote.views import * #vote/view.py �뿉 �엳�뒗 紐⑤뱺 �븿�닔/�겢�옒�뒪 異붽�
urlpatterns = [
    path('admin/', admin.site.urls),#127.0.0.1:8000/admin/
    path('', index, name = 'index' ),#127.0.0.1:8000/
    #URL �벑濡� �떆 �뙆�씠�뜫 肄붾뱶�뿉�꽌 URL�쓣 �쇅�썙�꽌 �궗�슜�븯吏� �븡怨�,
    #蹂꾩묶�쓣 �씠�슜�빐�꽌 �궗�슜�븷 �닔 �엳�룄濡� name 留ㅺ컻蹂��닔�뿉 臾몄옄�뿴�쓣 ���엯
    path('<int:question_id>/', detail, name = 'detail' ),
    #path('admin/',index),
    #URL 異붽� http://127.0.0.1:8000 二쇱냼濡� �젒洹쇱떆 vote �뼱�뵆由ъ��씠�뀡�쓽
    #view�씤 index �븿�닔瑜� �샇異� �븯�룄濡� �벑濡�
    path('result/<int:question_id>/',result, name='result'),
    path('vote/',vote,name='vote'),
    path('registerQuestion/', registerQ, name='registerQ'),
    path('registerChoice/', registerC, name='registerC'),
    path('delete/<int:question_id>/',deleteQ,name='deleteQ'),
    path('deleteC/<int:choice_id>/',deleteC, name='deleteC'),
    path('updateQ/<int:question_id>/',updateQ,name="updateQ"),
    path('updateC/<int:choice_id>/',updateC, name='updateC'),
    #127.0.0.1/login/ URL 二쇱냼濡� �슂泥��씠 �릺硫� view�븿�닔 �샇異� 泥섎━�뒗
    #customlogin �뤃�뜑�뿉�엳�뒗 urls.py�뿉�꽌 泥섎━�븯�룄濡� �벑濡�
    path('login/', include('customlogin.urls')),
    path('auth/',include('social_django.urls',namespace = 'social')),
    path('blog/',include('blog.urls'))
]

#파일 관리 모듈 : numpy
from django.conf import settings
from django.conf.urls.static import static
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)









