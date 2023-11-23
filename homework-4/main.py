from src.video import Video, PLVideo


if __name__ == '__main__':
    video1 = Video('AWX4JnAnjBE')
    video2 = PLVideo('4fObz_qw9u4', 'PLv_zOGKKxVph_8g2Mqc3LMhj0M_BfasbC')
    print(video1.title)
    print(video2)
    assert str(video1.title) == 'GIL в Python: зачем он нужен и как с этим жить'
    assert str(video2.title) == 'MoscowPython Meetup 78 - вступление'
