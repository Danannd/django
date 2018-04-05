from animation.models import Infobox
from animation.models import News
from animation.serializer import InfoboxSerializer
from animation.serializer import NewsSerializer
from rest_framework import generics


class AnimationList(generics.ListCreateAPIView):
    queryset = Infobox.objects.all()
    serializer_class = InfoboxSerializer


class NewsList(generics.ListCreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer


class AnimationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Infobox.objects.all()
    serializer_class = InfoboxSerializer