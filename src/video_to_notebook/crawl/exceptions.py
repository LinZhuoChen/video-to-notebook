"""Crawler exceptions shared across platform adapters."""
from __future__ import annotations


class BilibiliCookieError(RuntimeError):
    """Raised when Bilibili rejects the request due to missing/expired cookies."""


class PlaylistFetchError(RuntimeError):
    """Raised when yt-dlp fails to enumerate a playlist (e.g. 404, 403, invalid URL)."""
