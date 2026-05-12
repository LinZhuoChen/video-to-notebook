"""Crawler exceptions shared across platform adapters."""
from __future__ import annotations


class BilibiliCookieError(RuntimeError):
    """Raised when Bilibili rejects the request due to missing/expired cookies."""
