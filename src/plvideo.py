from video import Video


class PLVideo(Video):
    def __init__(self, video_id, playlist_id):
        super().__init__(video_id)
        self.playlist_id = playlist_id

    def __repr__(self):
        return f"PLVideo(id={self.video_id}, title={self.title}, views={self.views}, likes={self.likes}, playlist_id={self.playlist_id})"

    def __str__(self):
        return f"{self.title} ({self.video_url}) - Views: {self.views}, Likes: {self.likes}, Playlist ID: {self.playlist_id}"

