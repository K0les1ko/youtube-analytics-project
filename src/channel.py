import os
import json
from googleapiclient.discovery import build

class Channel:
    DEVELOPER_KEY = 'AIzaSyBgM_QMOxIgBaTz56iO5LSodb_L-vypyrk'
    YOUTUBE_API_SERVICE_NAME = 'youtube'
    YOUTUBE_API_VERSION = 'v3'
    all = []

    def __init__(self, channel_id):
        self.channel_id = channel_id
        self.data = self.get_channel_data()

        self.id = self.channel_id
        self.title = self.data['snippet']['title']
        self.description = self.data['snippet']['description']
        self.url = f"https://www.youtube.com/channel/{self.channel_id}"
        self.subscriber_count = self.data['statistics']['subscriberCount']
        self.video_count = self.data['statistics']['videoCount']
        self.view_count = self.data['statistics']['viewCount']

    def get_channel_data(self):
        youtube = self.get_service()
        results = youtube.channels().list(
            part='snippet,statistics',
            id=self.channel_id
        ).execute()

        if 'items' in results:
            return results['items'][0]
        else:
            return None

    @classmethod
    def get_service(cls):
        return build(
            cls.YOUTUBE_API_SERVICE_NAME,
            cls.YOUTUBE_API_VERSION,
            developerKey=cls.DEVELOPER_KEY
        )

    def to_json(self, filename):
        channel_data = {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'link': self.url,
            'subscriber_count': self.subscriber_count,
            'video_count': self.video_count,
            'view_count': self.view_count
        }

        if self.data:
            with open(filename, 'w', encoding='utf-8') as file:
                json.dump(channel_data, file, indent=2, ensure_ascii=False)
                return True
        return False

    @staticmethod
    def string_to_number(value: str) -> float:
        """
        Преобразует строку в число.

        :param value: Строка, представляющая число.
        :return: Преобразованное число.
        """
        try:
            return int(float(value))
        except ValueError:
            return 0.0

# Очищаем список all в начале метода
Channel.all = []
