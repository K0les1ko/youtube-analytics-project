import requests
from datetime import timedelta

class Video:
    def __init__(self, video_id):
        self.video_id = video_id
        self.title = ""
        self.video_url = ""
        self.duration = timedelta()
        self.views = 0
        self.likes = 0
        self._load_video_info()

    def _load_video_info(self):
        api_key = "AIzaSyBgM_QMOxIgBaTz56iO5LSodb_L-vypyrk"
        url = f"https://www.googleapis.com/youtube/v3/videos?part=snippet,contentDetails,statistics&id={self.video_id}&key={api_key}"
        response = requests.get(url)
        data = response.json()

        if "items" in data and data["items"]:
            snippet = data["items"][0]["snippet"]
            self.title = snippet.get("title", "")

            content_details = data["items"][0]["contentDetails"]
            duration_str = content_details.get("duration", "PT0S")
            self.duration = self._parse_duration(duration_str)

            statistics = data["items"][0]["statistics"]
            self.views = int(statistics.get("viewCount", 0))
            self.likes = int(statistics.get("likeCount", 0))

    def _parse_duration(self, duration_str):
        # Преобразование строки продолжительности в timedelta
        minutes, seconds = map(int, duration_str[2:-1].split('M')[1].split('S'))
        return timedelta(minutes=minutes, seconds=seconds)



    def __repr__(self):
        return f"Video(id={self.video_id}, title={self.title}, views={self.views}, likes={self.likes})"

    def __str__(self):
        return f"{self.title} ({self.video_url}) - Views: {self.views}, Likes: {self.likes}"


