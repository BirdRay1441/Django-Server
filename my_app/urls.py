from django.urls import path, re_path
from my_app import views 

urlpatterns = [
    path('', views.index, name='index'),
    # path('continents/', views.ContinentList.as_view()),
    # path('countries/', views.CountryList.as_view()),
    # path('cities/', views.CityList.as_view()),
    # path('weathers/', views.WeatherList.as_view()),
    path('logout/', views.user_logout, name="logout"),
    path('special/', views.special, name="special"),
    path('register/', views.register, name="register"),
    path('login/', views.user_login, name="user_login"),
    path('lection/<TypeID>/', views.MaterialsListView.as_view(), name='type'),
]