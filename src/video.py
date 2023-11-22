import requests


class Video:
    def __init__(self, video_id):
        self.video_id = video_id
        self.title = ""
        self.video_url = ""
        self.views = 0
        self.likes = 0
        self._load_video_info()

    def _load_video_info(self):
        api_key = "AIzaSyBgM_QMOxIgBaTz56iO5LSodb_L-vypyrk"
        url = f"https://www.googleapis.com/youtube/v3/videos?part=snippet,statistics&id={self.video_id}&key={api_key}"
        response = requests.get(url)
        data = response.json()

        if "items" in data and data["items"]:
            snippet = data["items"][0]["snippet"]
            self.title = snippet.get("title", "")
            self.video_url = f"https://www.youtube.com/watch?v={self.video_id}"

        if "items" in data and data["items"]:
            statistics = data["items"][0]["statistics"]
            self.views = int(statistics.get("viewCount", 0))
            self.likes = int(statistics.get("likeCount", 0))

    def __repr__(self):
        return f"Video(id={self.video_id}, title={self.title}, views={self.views}, likes={self.likes})"

    def __str__(self):
        return f"{self.title} ({self.video_url}) - Views: {self.views}, Likes: {self.likes}"


class PLVideo(Video):
    def __init__(self, video_id, playlist_id):
        super().__init__(video_id)
        self.playlist_id = playlist_id

    def __repr__(self):
        return f"PLVideo(id={self.video_id}, title={self.title}, views={self.views}, likes={self.likes}, playlist_id={self.playlist_id})"

    def __str__(self):
        return f"{self.title} ({self.video_url}) - Views: {self.views}, Likes: {self.likes}, Playlist ID: {self.playlist_id}"



