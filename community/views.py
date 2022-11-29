from django.shortcuts import render
from .forms import Form
from .models import Article
# Create your views here.
def write(request):
  # request의 post true이면
  # 사용자가 입력한 form 데이터를 변수에 저장
  # ORM으로 DB에 저장하기
  if request.method == 'POST':
    form = Form(request.POST)
    if form.is_valid():
      form.save() # 필드값 저장함.
  else:
    form = Form()
  return render(request, 'write.html', {'form': form}) 
  # 비즈니스 로직 구현
  # data ={'키':'값'}
  # return render(request, 'html템플릿 파일.html',data)

  # return render(request, 'write.html', {'data': hello, 'data2':hello2})
def articleList(request):
  article_list = Article.objects.all()
  return render(request, 'list.html', {'article_list': article_list})

def viewDetail(request, num=1):
  # 클릭한 레코드를 DB 읽어오기 
  article_detail = Article.objects.get(id=num)
  # article_detail = get_object_or_404(Article, id=num)
  return render(request, 'view_detail.html', {'article_detail': article_detail})