from django.db import models


# 웹툰의 정보를 저장하는 테이블
class Webtoon(models.Model):
    WebtoonID = models.TextField()
    Title = models.TextField()
    Description = models.TextField()
    Age = models.IntegerField()
    Stars = models.FloatField()
    End = models.BooleanField()
    Round = models.IntegerField()
    WebLink = models.TextField()  # 웹툰 플랫폼의 링크
    CharLink = models.TextField()  # 캐릭터 이미지를 가져오는 링크
    BackLink = models.TextField()  # 배경 이미지를 가져오는 링크


# 웹툰 작가를 저장하는 테이블
class Author(models.Model):
    Name = models.TextField()


# 웹툰 장르를 저장하는 테이블
class Genre(models.Model):
    Genre = models.TextField()


# 웹툰 플랫폼을 저장하는 테이블
class Platform(models.Model):
    ComName = models.TextField()


# 웹툰과 작가를 연결하는 테이블
class WebAu(models.Model):
    Web = models.ForeignKey("Webtoon", on_delete=models.CASCADE)
    Au = models.ForeignKey("Author", on_delete=models.SET_NULL, null=True)


# 웹툰과 장르를 연결하는 테이블
class WebGen(models.Model):
    Web = models.ForeignKey("Webtoon", on_delete=models.CASCADE)
    Gen = models.ForeignKey("Genre", on_delete=models.SET_NULL, null=True)


# 웹툰과 플랫폼을 연결하는 테이블
class WebPlat(models.Model):
    Web = models.ForeignKey("Webtoon", on_delete=models.CASCADE)
    Plat = models.ForeignKey("Platform", on_delete=models.SET_NULL, null=True)
