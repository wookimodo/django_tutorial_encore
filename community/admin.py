from django.contrib import admin

# Register your models here.
from .models import Article

class ArticleAdmin(admin.ModelAdmin):
  # fields = ['name', 'title', 'contents', 'url', 'email', 'owner']
  list_display = ('pk', 'name', 'title','cdate')
  list_filter = ['cdate']
  search_fields = ['name', 'title']
  fieldsets = [
    ('제목' , {'fields': ['title']}), 
    ('내용', {'fields':['contents']}), 
    ('작성자 정보', {'fields':['name', 'url', 'email']}), 
    ('작성자 id', {'fields':['owner'], 'classes':['collapse']}), 
  ]


# admin 페이지에 Article 데이터 모델 등록
admin.site.register(Article, ArticleAdmin)