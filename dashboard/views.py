from django.shortcuts import render, redirect
from .models import CountryData
from .forms import CountryDataForm

#views는 데이터를 핸들링 하는곳

# Create your views here.
def dashboard(request):
    # if request method = post
    # valid한다면
    # 폼에 입력 데이터를 저장
    # else 
    #   폼객체를 생성 
    #   폼객체 랜더링
    if request.method == 'POST':
        form = CountryDataForm(request.POST)
        # print(form) # form이 어떻게 찍히는지 확인.
        if form.is_valid():
            '''
            [중복제크]
            폼에 입력 값을 개별로 변수 대입
            나라이름(country) DB 깂이 있는지 확인
            입력한 나라 이름이 있으면, 업데이트하고 
            없으면 저장 
            '''
            input_country = form.data.get('country', None)
            input_num = form.data.get('population', None)
            # print(input_country, input_num) # 값이 어떻게 찍히는지 확인
            CountryData.objects.update_or_create( #중복체크 _or_
            #filter
            country = input_country,
            #new value
            defaults= {
                'country': input_country,
                'population': input_num
            }
            )
            # form.save() #db저장
            # return redirect('/dashboard')
            return redirect('.')
    else:
        form = CountryDataForm()

    # 나라별 인구 데이터 DB에서 가져오기
    country_datas = CountryData.objects.all()
    # print(country_datas) # 데이터가 잘나오는지 확인
    context = {
        'form': form,
        'country_datas':country_datas
    }
    return render(request, 'dashboard/dashboard.html',context)