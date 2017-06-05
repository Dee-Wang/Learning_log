"""定义learning_logs的URL模式"""

from django.conf.urls import include, url
from . import views

urlpatterns = [
    #主页
    url(r'^$', views.index, name = 'index'),

    #显示所有的主题
    url(r'^topics/$', views.topics, name = 'topics'),

    #显示所有的列表
    url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name = 'topic'),
   
    #用于添加新的主题
    url(r'^new_topic/$', views.new_topic, name = 'new_topic'),

    #用于添加新的条目
    url(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name = 'new_entry'),
  
    #用于编辑现有的条目
    url(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name = 'edit_entry'),

]
