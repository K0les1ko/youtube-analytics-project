import os
import json
from googleapiclient.discovery import build

class Channel:
    DEVELOPER_KEY = 'AIzaSyBgM_QMOxIgBaTz56iO5LSodb_L-vypyrk'
    YOUTUBE_API_SERVICE_NAME = 'youtube'
    YOUTUBE_API_VERSION = 'v3'
    all = []

    def __init__(self, channel_id, title='', description='', subscriber_count=0):
        self.channel_id = channel_id
        self.data = self.get_channel_data()

        self.id = self.channel_id
        self.title = title or self.data['snippet']['title']
        self.description = description or self.data['snippet']['description']
        self.url = f"https://www.youtube.com/channel/{self.channel_id}"
        self.subscriber_count = subscriber_count or self.string_to_number(self.data['statistics']['subscriberCount'])
        self.video_count = self.string_to_number(self.data['statistics']['videoCount'])
        self.view_count = self.string_to_number(self.data['statistics']['viewCount'])

    def __repr__(self):
        return f"Channel(id={self.id}, title={self.title}, subscriber_count={self.subscriber_count})"

    def __str__(self):
        return f"{self.title} ({self.url}) - Subscribers: {self.subscriber_count}"

    def __add__(self, other):
        if isinstance(other, Channel):
            return Channel(self.channel_id, f"{self.title} + {other.title}", "", self.subscriber_count + other.subscriber_count)
        raise TypeError("Unsupported operand type for +")

    def __sub__(self, other):
        if isinstance(other, Channel):
            return Channel(self.channel_id, f"{self.title} - {other.title}", "", self.subscriber_count - other.subscriber_count)
        raise TypeError("Unsupported operand type for -")

    def __eq__(self, other):
        if isinstance(other, Channel):
            return self.subscriber_count == other.subscriber_count
        return False

    def __lt__(self, other):
        if isinstance(other, Channel):
            return self.subscriber_count < other.subscriber_count
        raise TypeError("Unsupported operand type for <")

    def __le__(self, other):
        if isinstance(other, Channel):
            return self.subscriber_count <= other.subscriber_count
        raise TypeError("Unsupported operand type for <=")

    def __gt__(self, other):
        if isinstance(other, Channel):
            return self.subscriber_count > other.subscriber_count
        raise TypeError("Unsupported operand type for >")

    def __ge__(self, other):
        if isinstance(other, Channel):
            return self.subscriber_count >= other.subscriber_count
        raise TypeError("Unsupported operand type for >=")

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
        try:
            return int(float(value))
        except ValueError:
            return 0.0

# Очищаем список all в начале метода
Channel.all = []