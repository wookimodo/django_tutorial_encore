from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Article(models.Model):
  name = models.CharField(max_length=50)
  title = models.CharField(max_length=50)
  contents = models.TextField()
  url = models.URLField()
  email = models.EmailField()
  cdate = models.DateTimeField(auto_now_add = True)
  mdate = models.DateTimeField(auto_now=True)
  # User테이블과 연결.
  # on_delete=models.CASCADE -> user가 삭제되면 user의 글도 같이 삭제되게.
  # blank=True -> 작성자가 없는 글도 허용하겠다.
  owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

  
  class Meta:
    # 관리자 테이블의 title바꾸는 것.
    verbose_name_plural = "아티클 작성하기"
    # 수정한 날짜 기준으로 정렬. 최근 글이 위로 오게.
    ordering = ('-mdate',)
    
  def __str__(self):
    return f"{self.title} -- {self.name} -- {self.cdate}"
  
  # models.Model에 내장되어 있는 함수임.
  # 모델의 개별 데이터 rul을 문자열로 반환. 
  # args=(self.id,) -> id를 문자열로 반환. 원래 id는 int.
  def get_absolute_url(self):
    return reverse('community:view_detail', args=(self.id,))
