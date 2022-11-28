from django.shortcuts import render

# Create your views here.
def write(request):
  # 비즈니스 로직 구현
  # data ={'키':'값'}
  # return render(request, 'html템플릿 파일.html',data)
  hello = "헬로 django"
  hello2 = "알고보니 쉬운 장고"
  return render(request, 'write.html', {'data': hello, 'data2':hello2})
