from django.contrib import admin

# Register your models here.
from .models import Article

# admin 페이지에 Article 데이터 모델 등록
admin.site.register(Article)