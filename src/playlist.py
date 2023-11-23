import requests
from datetime import timedelta
from video import Video
from plvideo import PLVideo

class PlayList:
    def __init__(self, playlist_id):
        self.playlist_id = playlist_id
        self.title = ""
        self.url = f"https://www.youtube.com/playlist?list={playlist_id}"
        self.videos = []
        self._load_playlist_info()

    def _load_playlist_info(self):
        api_key = "AIzaSyBgM_QMOxIgBaTz56iO5LSodb_L-vypyrk"
        url = f"https://www.googleapis.com/youtube/v3/playlists?part=snippet&id={self.playlist_id}&key={api_key}"
        response = requests.get(url)
        data = response.json()

        if "items" in data and data["items"]:
            snippet = data["items"][0]["snippet"]
            self.title = snippet.get("title", "Title not available")


        self._load_videos()

    def _load_videos(self):
        api_key = "AIzaSyBgM_QMOxIgBaTz56iO5LSodb_L-vypyrk"
        url = f"https://www.googleapis.com/youtube/v3/playlistItems?part=contentDetails&maxResults=50&playlistId={self.playlist_id}&key={api_key}"
        response = requests.get(url)
        data = response.json()

        video_ids = [item["contentDetails"]["videoId"] for item in data.get("items", [])]
        self.videos = [PLVideo(video_id, self.playlist_id) for video_id in video_ids]

    @property
    def total_duration(self):
        total_duration = sum((video.duration for video in self.videos), timedelta())

        return total_duration

    def show_best_video(self):
        if not self.videos:
            return None
        best_video = max(self.videos, key=lambda video: video.likes)
        return best_video.video_url
