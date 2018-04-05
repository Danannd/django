from django.conf.urls import url
from animation import views, views_generic
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^animation/$', views_generic.AnimationList.as_view()),
    url(r'^animation/detail/character/ani_id=(?P<ani_id>[0-9]+)/$', views.anime_bangumicharacter),
    url(r'^animation/detail/staff/ani_id=(?P<ani_id>[0-9]+)/$', views.anime_bangumistaff),
    url(r'^news/$', views_generic.NewsList.as_view()),
    url(r'^animation/this_season/$', views.anime_this_season),
    url(r'^animation/ani_id=(?P<pk>[0-9]+)/$', views.anime_detail),
    url(r'^animation/name_cn=(?P<name_cn>(.)+)/$', views.anime_name_cn),
    url(r'^score/ani_id=(?P<bgm_id>[0-9]+)/$', views.anime_score),
    url(r'^news/news_id=(?P<news_id>[0-9]+)/$', views.anime_news),
]

urlpatterns = format_suffix_patterns(urlpatterns)
