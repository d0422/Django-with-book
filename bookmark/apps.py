#앱의 설정 클래스를 정의하는 파일
from django.apps import AppConfig


class BookmarkConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bookmark'
