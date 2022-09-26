from django.urls import path
from . import views
from .feeds import LatestPostsFeed
#crea tus urls de la app

app_name= 'blog'
urlpatterns = [
	path('',  views.post_list, name="post_list"),
	path('<int:post_id>/<slug:post_slug>/',views.post_detail, name='post_detail'),
	path('<int:post_id>/<slug:post_slug>/share/',views.post_share, name='post_share'),
	path('category/<int:category_id>/<slug:post_slug>/', views.category, name="category"),

	path('reply/<int:comment_id>/',views.commet_reply, name='commet_reply'),

	path('tag/<slug:tag_slug>/', views.post_list, name='post_list_by_tag'),

	path('feed/', LatestPostsFeed(), name='post_feed'),
	path('search/', views.post_search, name='post_search'),



]