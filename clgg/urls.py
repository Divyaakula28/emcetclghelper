from clgg import views
from django.urls import path, include

urlpatterns = [
    path('findurclg/',views.findurclg,name='findurclg'),
    path('table/',views.table,name='table'),
    path('test/',views.test,name='test'),
    path('table1/',views.table1,name='table1'),
    path('but1/',views.but1,name='but1'),
]