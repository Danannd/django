from django.db import models


class Infobox(models.Model):
    ani_id = models.IntegerField(primary_key=True)
    ani_type = models.CharField(blank=True, max_length=100)
    name_jp = models.CharField(blank=True, max_length=100)
    name_cn = models.CharField(blank=True, max_length=100)
    total_episode = models.CharField(blank=True, max_length=100)
    broadcast_time = models.CharField(blank=True, max_length=100)
    broadcast_over = models.CharField(blank=True, max_length=100)
    broadcast_state = models.CharField(blank=True, max_length=100)
    original = models.CharField(blank=True, max_length=100)
    director = models.CharField(blank=True, max_length=100)
    script = models.CharField(blank=True, max_length=500)
    storyboard = models.CharField(blank=True, max_length=500)
    perform = models.CharField(blank=True, max_length=500)
    music = models.CharField(blank=True, max_length=100)
    character_original_bill = models.CharField(blank=True, max_length=100)
    character_design = models.CharField(blank=True, max_length=100)
    machine_design = models.CharField(blank=True, max_length=100)
    art_director = models.CharField(blank=True, max_length=100)
    color_design = models.CharField(blank=True, max_length=100)
    animation_director = models.CharField(blank=True, max_length=500)
    photo_director = models.CharField(blank=True, max_length=100)
    original_painting = models.CharField(blank=True, max_length=1000)
    sec_original_painting = models.CharField(blank=True, max_length=100)
    animate_check = models.CharField(blank=True, max_length=100)
    background_art = models.CharField(blank=True, max_length=100)
    color_designation = models.CharField(blank=True, max_length=100)
    theme_arranger = models.CharField(blank=True, max_length=100)
    theme_word = models.CharField(blank=True, max_length=100)
    theme_compose = models.CharField(blank=True, max_length=100)
    special_effect = models.CharField(blank=True, max_length=100)
    design = models.CharField(blank=True, max_length=100)
    edit = models.CharField(blank=True, max_length=100)
    audio_director = models.CharField(blank=True, max_length=100)
    audio = models.CharField(blank=True, max_length=100)
    sound_effect = models.CharField(blank=True, max_length=100)
    movemaking = models.CharField(blank=True, max_length=100)
    production = models.CharField(blank=True, max_length=100)
    production_support = models.CharField(blank=True, max_length=100)
    animate_production = models.CharField(blank=True, max_length=100)
    sec_director = models.CharField(blank=True, max_length=100)
    another_name = models.CharField(blank=True, max_length=100)
    releast_time = models.CharField(blank=True, max_length=100)
    official_web = models.CharField(blank=True, max_length=500)
    broadcast_tv = models.CharField(blank=True, max_length=100)
    scriptwriter = models.CharField(blank=True, max_length=100)
    layout = models.CharField(blank=True, max_length=100)
    information = models.CharField(blank=True, max_length=3000)
    bilibili_bc = models.IntegerField(blank=True, default=-1)
    acfun_bc = models.IntegerField(blank=True, default=-1)
    iqiyi_bc = models.IntegerField(blank=True, default=-1)
    letv_bc = models.IntegerField(blank=True, default=-1)
    tencent_bc = models.IntegerField(blank=True, default=-1)
    youku_bc = models.IntegerField(blank=True, default=-1)

    def __str__(self):
        return self.name_cn


class Person(models.Model):
    person_id = models.IntegerField(primary_key=True)
    name_jp = models.CharField(blank=True, max_length=100, default="")
    name_cn = models.CharField(blank=True, max_length=100, default="")
    profession = models.CharField(blank=True, max_length=50, default="")
    sex = models.CharField(blank=True, max_length=10, default="")
    blood = models.CharField(blank=True, max_length=10, default="")
    birthday = models.CharField(blank=True, max_length=50, default="")
    height = models.CharField(blank=True, max_length=10, default="")
    homeplace = models.CharField(blank=True, max_length=100, default="")
    office = models.CharField(blank=True, max_length=100, default="")
    hp = models.CharField(blank=True, max_length=100, default="")
    twitter = models.CharField(blank=True, max_length=50, default="")
    pixiv = models.CharField(blank=True, max_length=50, default="")
    information = models.CharField(blank=True, max_length=5000, default="")

    def __str__(self):
        return self.name_jp


class Character(models.Model):
    character_id = models.IntegerField(primary_key=True)
    name_jp = models.CharField(blank=True, max_length=100, default="")
    name_cn = models.CharField(blank=True, max_length=100, default="")
    sex = models.CharField(blank=True, max_length=10, default="")
    birthday = models.CharField(blank=True, max_length=50, default="")
    height = models.CharField(blank=True, max_length=10, default="")
    weight = models.CharField(blank=True, max_length=10, default="")
    constellation = models.CharField(blank=True, max_length=50, default="")
    bwh = models.CharField(blank=True, max_length=20, default="")
    information = models.CharField(blank=True, max_length=5000, default="")

    def __str__(self):
        return self.name_jp


class Bangumi_character(models.Model):
    id = models.IntegerField(primary_key=True)
    ani_id = models.IntegerField(blank=True, default=0)
    character_id = models.IntegerField(blank=True, default=0)
    person_id = models.IntegerField(blank=True, default=0)
    person2_id = models.IntegerField(blank=True, default=0)
    ani_name_jp = models.CharField(blank=True, max_length=100, default="")
    ani_name_cn = models.CharField(blank=True, max_length=100, default="")
    character_name_jp = models.CharField(blank=True, max_length=100, default="")
    character_name_cn = models.CharField(blank=True, max_length=100, default="")
    person_name_jp = models.CharField(blank=True, max_length=100, default="")
    person_name_cn = models.CharField(blank=True, max_length=100, default="")
    person2_name_jp = models.CharField(blank=True, max_length=100, default="")
    person2_name_cn = models.CharField(blank=True, max_length=100, default="")

    def __str__(self):
        return self.character_name_jp


class Bangumi_staff(models.Model):
    id = models.IntegerField(primary_key=True)
    ani_id = models.IntegerField(blank=True, default=0)
    person_id = models.IntegerField(blank=True, default=0)
    person_name_jp = models.CharField(blank=True, max_length=100, default="")
    person_name_cn = models.CharField(blank=True, max_length=100, default="")
    profession = models.CharField(blank=True, max_length=100, default="")

    def __str__(self):
        return self.person_name_jp



class Score(models.Model):
    bgm_id = models.IntegerField(primary_key=True)
    name_jp = models.CharField(blank=True, max_length=100, default="")
    bgm_score = models.FloatField(blank=True, default=0.0)
    bgm_votes = models.IntegerField(blank=True, default=0)
    anidb_id = models.IntegerField(blank=True, default=0)
    anidb_score = models.FloatField(blank=True, default=0.0)
    anidb_votes = models.IntegerField(blank=True, default=0)
    sachi_id = models.IntegerField(blank=True, default=0)
    sachi_score = models.FloatField(blank=True, default=0.0)
    sachi_votes = models.IntegerField(blank=True, default=0)
    ann_id = models.IntegerField(blank=True, default=0)
    ann_score = models.FloatField(blank=True, default=0.0)
    ann_votes = models.IntegerField(blank=True, default=0)
    mal_id = models.IntegerField(blank=True, default=0)
    mal_score = models.FloatField(blank=True, default=0.0)
    mal_votes = models.IntegerField(blank=True, default=0)
    ankr_id = models.IntegerField(blank=True, default=0)
    ankr_score = models.FloatField(blank=True, default=0.0)
    ankr_votes = models.IntegerField(blank=True, default=0)

    def __str__(self):
        return self.bgm_id

class News(models.Model):
    news_id = models.IntegerField(primary_key=True)
    news_title = models.CharField(blank=True, max_length=200, default="")
    news_content = models.TextField(blank=True, default="")
    news_datetime = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.news_title


