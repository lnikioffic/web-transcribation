from transcribation import get_audio_text


def test_not_void_file():
    assert len(get_audio_text('test_video.mp4')) >= 0


def test_void_file():
    assert len(get_audio_text('')) == 0
