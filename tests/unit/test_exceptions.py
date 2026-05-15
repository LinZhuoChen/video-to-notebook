from __future__ import annotations

import pytest

from video_to_notebook.crawl.exceptions import BilibiliCookieError


def test_bilibili_cookie_error_is_runtime_error():
    assert issubclass(BilibiliCookieError, RuntimeError)


def test_bilibili_cookie_error_raises():
    with pytest.raises(BilibiliCookieError) as exc:
        raise BilibiliCookieError("test message")
    assert "test message" in str(exc.value)


def test_backward_compat_import_from_bilibili():
    """The old import location must still work to avoid breaking callers."""
    from video_to_notebook.crawl.bilibili import BilibiliCookieError as B1
    from video_to_notebook.crawl.exceptions import BilibiliCookieError as B2
    assert B1 is B2
