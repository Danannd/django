from django.contrib import admin
from .models import Infobox
from .models import Score
from .models import News
from .models import Bangumi_character
from .models import Bangumi_staff

class InfoboxAdmin(admin.ModelAdmin):
    fields = ['ani_id', 'ani_type', 'name_jp', 'name_cn', 'total_episode', 'broadcast_time',
                  'broadcast_over', 'broadcast_state', 'original', 'director', 'script',
                  'storyboard', 'perform', 'music', 'character_original_bill', 'character_design',
                  'machine_design', 'art_director', 'color_design', 'animation_director',
                  'photo_director', 'original_painting', 'sec_original_painting', 'animate_check',
                  'background_art', 'color_designation', 'theme_arranger', 'theme_word',
                  'theme_compose', 'special_effect', 'design', 'edit', 'audio_director',
                  'audio', 'sound_effect', 'movemaking', 'production', 'production_support',
                  'animate_production', 'sec_director', 'another_name', 'releast_time',
                  'official_web', 'broadcast_tv', 'scriptwriter', 'layout', 'information']

class ScoreAdmin(admin.ModelAdmin):
    fields = ['name_jp', 'bgm_id', 'bgm_score', 'bgm_votes', 'anidb_id', 'anidb_score', 'anidb_votes',
                  'sachi_id', 'sachi_score', 'sachi_votes', 'ann_id', 'ann_score', 'ann_votes',
                  'mal_id', 'mal_score', 'mal_votes', 'ankr_id', 'ankr_score', 'ankr_votes']

class NewsAdmin(admin.ModelAdmin):
    fields = ['news_id', 'news_title', 'news_content', 'news_datetime']

class BangumiCharacterAdmin(admin.ModelAdmin):
    fields = ['id', 'ani_id', 'character_id', 'person_id', 'person2_id', 'ani_name_jp', 'ani_name_cn',
              'character_name_jp', 'character_name_cn', 'person_name_jp', 'person_name_cn',
              'person2_name_jp', 'person2_name_cn']


class BangumiStaffAdmin(admin.ModelAdmin):
    fields = ['id', 'ani_id', 'person_id', 'person_name_jp', 'person_name_cn', 'profession']



admin.site.register(Infobox, InfoboxAdmin)
admin.site.register(Score, ScoreAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(Bangumi_character, BangumiCharacterAdmin)
admin.site.register(Bangumi_staff, BangumiStaffAdmin)

