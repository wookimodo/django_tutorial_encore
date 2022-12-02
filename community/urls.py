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
    # /change/
    path('change/', views.ArticleChangeView.as_view(), name='change_list'),
    # /view_detail/1/update
    path('<int:pk>/update/', views.ArticleUpdateView.as_view(), name='article_update'),
    # /view_detail/1/delete
    path('<int:pk>/delete', views.ArticleDeleteView.as_view(), name='article_delete'),

]