from rest_framework import serializers
from animation.models import Infobox
from animation.models import Score
from animation.models import News
from animation.models import Bangumi_character
from animation.models import Bangumi_staff



class InfoboxSerializer(serializers.ModelSerializer):
    class Meta:
        model = Infobox
        fields = ('ani_id', 'ani_type', 'name_jp', 'name_cn', 'total_episode', 'broadcast_time',
                  'broadcast_over', 'broadcast_state', 'original', 'director', 'script',
                  'storyboard', 'perform', 'music', 'character_original_bill', 'character_design',
                  'machine_design', 'art_director', 'color_design', 'animation_director',
                  'photo_director', 'original_painting', 'sec_original_painting', 'animate_check',
                  'background_art', 'color_designation', 'theme_arranger', 'theme_word',
                  'theme_compose', 'special_effect', 'design', 'edit', 'audio_director',
                  'audio', 'sound_effect', 'movemaking', 'production', 'production_support',
                  'animate_production', 'sec_director', 'another_name', 'releast_time',
                  'official_web', 'broadcast_tv', 'scriptwriter', 'layout', 'information')


class ScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Score
        fields = ('bgm_id', 'bgm_score', 'bgm_votes', 'anidb_id', 'anidb_score', 'anidb_votes',
                  'sachi_id', 'sachi_score', 'sachi_votes', 'ann_id', 'ann_score', 'ann_votes',
                  'mal_id', 'mal_score', 'mal_votes', 'ankr_id', 'ankr_score', 'ankr_votes',
                  'name_jp')

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ('news_id', 'news_title', 'news_content', 'news_datetime')


class BangumiCharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bangumi_character
        fields = ('id', 'ani_id', 'character_id', 'person_id', 'person2_id', 'ani_name_jp', 'ani_name_cn',
              'character_name_jp', 'character_name_cn', 'person_name_jp', 'person_name_cn',
              'person2_name_jp', 'person2_name_cn')

class BangumiStaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bangumi_staff
        fields = ('id', 'ani_id', 'person_id', 'person_name_jp', 'person_name_cn', 'profession')