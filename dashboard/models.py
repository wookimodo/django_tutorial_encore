from django.db import models

# Create your models here.
class CountryData(models.Model):
  country = models.CharField(max_length=100)
  population = models.IntegerField()
  class Meta:
    verbose_name_plural = "각 나라별 인구 데이터"
# 객체를 생성할 때 object로 표현되지 않고 변수명을 지정하고 싶다면, 이렇게 하면 됨. 
  def __str__(self):
    return f'{self.country}--{self.population}'
# 모델에서 클래스를 생성했을 때나 수정을 했을 때는, 모델을 꼭 DB에 적용시켜줘야 한다. 
# models.py를 건드리면 makemigrations와 migrate를 꼭 해줘야된다고 생각하면 됨.
# 할 때마다 migrations에 버전이 생기면서 history가 생성됨.
