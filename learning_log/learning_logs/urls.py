"""定义learning_logs的URL模式"""
from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('topics', views.topics, name='topics'),
	# ex: /topic/1
    path('topic/<int:topic_id>', views.topic, name='topic'),
    path('topic/new', views.new_topic, name='new_topic'),
    path('topic/edit/<int:topic_id>', views.edit_topic, name='edit_topic'),
    # ex: /entry/new/1
    path('entry/new/<int:topic_id>', views.new_entry, name='new_entry'),
    path('entry/edit/<int:entry_id>', views.edit_entry, name='edit_entry'),
]