from course_merger.cli import _slug_from_url


def test_slug_from_youtube_playlist():
    assert _slug_from_url(
        "https://www.youtube.com/playlist?list=PLPTV0NXA_ZShnka8uVzF3mSvZdilfiGWG"
    ) == "plptv0nxa-zshnka8uvzf3msvzdilfigwg"


def test_slug_from_youtube_watch():
    assert _slug_from_url("https://www.youtube.com/watch?v=k2-_UQo97vo") == "k2-uqo97vo"


def test_slug_from_bilibili():
    assert _slug_from_url("https://www.bilibili.com/video/BV1xx411c7mD/") == "bv1xx411c7md"


def test_slug_fallback():
    s = _slug_from_url("https://example.com/foo/bar")
    assert s.startswith("course-") and len(s) > len("course-")
