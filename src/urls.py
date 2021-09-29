from src import views

from django.urls import path

urlpatterns = [
    path('getdata',views.home),#get data
    path('postdata/',views.postdata),
    path('ap/',views.StudentPostView().as_view()),
    path('apg/',views.StudentGetView().as_view()),
]