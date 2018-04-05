from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from animation.models import Infobox
from animation.models import Score
from animation.models import News
from animation.models import Bangumi_character
from animation.models import Bangumi_staff

from animation.serializer import InfoboxSerializer
from animation.serializer import ScoreSerializer
from animation.serializer import NewsSerializer
from animation.serializer import BangumiCharacterSerializer
from animation.serializer import BangumiStaffSerializer


@api_view(['GET', 'POST'])
def anime_list(request, format=None):
    """
    List animes all data, or create a new animes.
    :param request:
    :param format:
    :return:
    """
    if request.method == 'GET':
        anime = Infobox.objects.all()
        ser = InfoboxSerializer(anime, many=True)
        return Response(ser.data)

    elif request.method == 'POST':
        ser = InfoboxSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_201_CREATED)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST', 'DELETE'])
def anime_detail(request, pk, format=None):
    """
    Find, create or delete anime.
    :param request:
    :param pk:
    :param format:
    :return:
    """
    try:
        anime = Infobox.objects.get(pk=pk)
    except Infobox.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        ser = InfoboxSerializer(anime)
        return Response(ser.data)

    elif request.method == 'PUT':
        ser = InfoboxSerializer(anime, data=request.data)
        if anime.is_valid():
            ser.save()
            return Response(ser.data)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        anime.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def anime_name_cn(request, name_cn, format=None):
    try:
        anime = Infobox.objects.filter(name_cn__contains=name_cn)
    except Infobox.DoesNotExist:
        return Response(status=status.HTTP_204_NO_CONTENT)

    if request.method == 'GET':
        ser = InfoboxSerializer(anime, many=True)
        return Response(ser.data)

@api_view(['GET'])
def anime_this_season(request, format=None):
    try:
        anime = Infobox.objects.filter(broadcast_time__contains="2018")
    except Infobox.DoesNotExist:
        return Response(status=status.HTTP_204_NO_CONTENT)

    if request.method == 'GET':
        ser = InfoboxSerializer(anime, many=True)
        return Response(ser.data)


@api_view(['GET'])
def anime_animation_id(request, animation_id, format=None):
    try:
        anime = Infobox.objects.get(animation_id=animation_id)
    except:
        return Response(status=status.HTTP_204_NO_CONTENT)

    if request.method == 'GET':
        ser = InfoboxSerializer(anime)
        return Response(ser.data)


@api_view(['GET'])
def anime_score(request, bgm_id, format=None):
    try:
        score = Score.objects.get(bgm_id=bgm_id)
    except:
        return Response(status=status.HTTP_204_NO_CONTENT)

    if request.method == 'GET':
        ser = ScoreSerializer(score)
        return Response(ser.data)

@api_view(['GET'])
def anime_news(request, news_id, format=None):
    try:
        news = News.objects.get(news_id=news_id)
    except:
        return Response(status=status.HTTP_204_NO_CONTENT)

    if request.method == 'GET':
        ser = NewsSerializer(news)
        return Response(ser.data)

@api_view(['GET'])
def anime_bangumicharacter(request, ani_id, format=None):
    try:
        bangumicharacter = Bangumi_character.objects.filter(ani_id=ani_id)
    except:
        return Response(status=status.HTTP_204_NO_CONTENT)

    if request.method == 'GET':
        ser = BangumiCharacterSerializer(bangumicharacter, many=True)
        return Response(ser.data)


@api_view(['GET'])
def anime_bangumistaff(request, ani_id, format=None):
    try:
        bangumistaff = Bangumi_staff.objects.filter(ani_id=ani_id)
    except:
        return Response(status=status.HTTP_204_NO_CONTENT)

    if request.method == 'GET':
        ser = BangumiStaffSerializer(bangumistaff, many=True)
        return Response(ser.data)
