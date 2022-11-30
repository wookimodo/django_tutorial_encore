from django.forms import ModelForm
from .models import CountryData

class CountryDataForm(ModelForm):
  class Meta:
  # model, fiedls는 ModelForm에 정의되어 있는 속성들임.
    model = CountryData
    # 이 테이블의 모든 필드를 모두 쓰겠다는 것.
    fields = '__all__'