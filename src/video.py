class Video:
    def __init__(self, video_id, title='', video_url='', views=0, likes=0):
        self.video_id = video_id
        self.title = title
        self.video_url = video_url
        self.views = views
        self.likes = likes

    def __repr__(self):
        return f"Video(id={self.video_id}, title={self.title}, views={self.views}, likes={self.likes})"

    def __str__(self):
        return f"{self.title} ({self.video_url}) - Views: {self.views}, Likes: {self.likes}"


class PLVideo(Video):
    def __init__(self, video_id, playlist_id, title='', video_url='', views=0, likes=0):
        super().__init__(video_id, title, video_url, views, likes)
        self.playlist_id = playlist_id

    def __repr__(self):
        return f"PLVideo(id={self.video_id}, title={self.title}, views={self.views}, likes={self.likes}, playlist_id={self.playlist_id})"

    def __str__(self):
        return f"{self.title} ({self.video_url}) - Views: {self.views}, Likes: {self.likes}, Playlist ID: {self.playlist_id}"
