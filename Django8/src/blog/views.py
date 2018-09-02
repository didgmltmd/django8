from django.shortcuts import render, get_object_or_404
from .models import *
from .forms import *
from django.http.response import HttpResponseRedirect
# Create your views here.


#제네릭 뷰 : 장고에서 제공하는 여러가지 기능을 하는 뷰클래스
#class 뷰이름(제네릭뷰):
from django.views.generic.list import ListView
#ListView : 특정 객체의 목록을 다루는 긴응ㄹ을 가진 제네릭 뷰
class index(ListView):
    #template_name : html 파일의 경로를 문자열로 저장 변수
    tempelete_name = 'blog/index.html'
    #model : 어떤 모델클래스의 객체를 리스트업 할 건지 명시하는 변수
    model = Post
    #context_object : 텔플릿에서 사용할 객체 리스트를 저장한 변수명
    context_object_name = 'list'
    #paginate_by : 한페이지에 몇개의 객체가 보여질지 설정하는 변수
    paginate_by = 5
    
def detail(request,post_id): 
    obj = get_object_or_404(Post,pk=post_id)
    return render(request,"blog/detail.html",{'post':obj})
    
def searchP(request):
    #<input type="text" name"query"/>
    #GET 요청으로 온 데이터에서 name속성이 'query'인 데이터 추출
    #name속성이'query'인 속성이 없으면 기본값으로 '' 반환
    q = request.GET.get('query','')
    t = request.GET.get('type','0')
    #'0' : 제목 검색
    if t=='0':
        #Post.objects.filter() : 특정 조건을 만족하는 Post객체 추출
        #filter.exclude.get 함수 사용시 : 모델클래스에 정의한 변수명_명령어 = 값
        #contains : 우변값에 해당하는 문자열이 해당 객테의 변수에 저장되있는지 확인
        list = Post.objects.filter(headline__contains=q)
        return render(request,'blog/searchP.html',{'list':list})
    #'1' : 내용검색
    elif t=='1':
        Post.objects.filter(content__contains=q)
        return render(request,'blog/serachP.html',{'list':list})
    
    
    