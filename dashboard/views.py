from django.shortcuts import render
from .models import CountryData
from .forms import CountryDataForm

# Create your views here.
def dashboard(request):
  # 나라별 인구 데이터를 DB에서 가져오기
  country_datas = CountryData.objects.all()
  # post이고 valid하다면, 폼에 입력 데이터를 저장
  if request.method == 'POST':
    form = CountryDataForm(request.POST) 
    if form.is_valid():
      form.save() # db 저장
  # 아닌경우는 빈 폼, 비어있으면 get방식이라서 여기 걸림.
  else: 
    form = CountryDataForm()

  context = {
    'country_datas' : country_datas,
    'form' : form
  }
  return render(request,'dashboard/dashboard.html', context)