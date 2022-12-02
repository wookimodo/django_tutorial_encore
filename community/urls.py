from django.urls import path
from community import views

app_name = 'community'

urlpatterns = [
    # /write/
    path('write/', views.WriteFormView.as_view(), name='write'),
    # path('write/', write, name='write'),
    # /list/
    path('list/', views.ArticleListView.as_view(), name='list'),
    # path('list/', views.articleList, name='list'),
    # /view_detail/1/
    path('view_detail/<slug:pk>/', views.ArticleDetailView.as_view(), name='view_detail'),
    # path('view_detail/<int:num>/', views.viewDetail, name='view_detail'),
]