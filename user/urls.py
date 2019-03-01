from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from user import views

urlpatterns =[

    path('user/', views.UserList.as_view(), name ="user-list"),
    path('user/<int:pk>/', views.UserDetail.as_view(),name = 'user-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
