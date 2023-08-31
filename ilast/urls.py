from django.urls import path
from . import views
from .views import search_view


app_name = 'ilast'


urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('post/', views.CreateIlastView.as_view(), name='post'),
    path('post_done/',
          views.PostSuccessView.as_view(), 
          name='post_done'),
    path('ilasts/<int:category>',
         views.CategoryView.as_view(),
         name = 'ilasts_cat'
         ),
    path('user-list/<int:user>',
         views.UserView.as_view(),
         name = 'user_list'
         ), 
    path('ilast-detail/<int:pk>',
         views.DetailView.as_view(),
         name='ilast_detail'
     ),
     path('mypage/', 
          views.MypageView.as_view(), 
          name = 'mypage'),
     path('ilast-delete/<int:pk>',
          views.IlastDeleteView.as_view(),
          name='ilast_delete'),
     path('', views.IndexView.as_view(), name='top'),
     path('ilast-edit/<int:pk>/', views.IlastEditView.as_view(), name='ilast_edit'),
     path('search/', views.search_view, name='search_results'),
]
