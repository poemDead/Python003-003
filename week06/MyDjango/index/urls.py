from django.urls import path,re_path, register_converter
from . import views

urlpatterns = [
    path('', views.index),

    # 带变量匹配
    # path('<int:year>', views.year)
    #  # 只接收整数，其他类型返回404
    path('<int:year>', views.year),
    path('<int:year>/<str:name>', views.name),

    # 正则表达
    re_path('(?P<year>[0-9]{4}).html', views.myyear, name='urlyear'),

]
