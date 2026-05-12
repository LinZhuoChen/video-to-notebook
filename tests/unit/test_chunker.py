from __future__ import annotations

from course_merger.crawl.base import Chunk, Chunker
from course_merger.crawl.subtitles import Cue


def _mk_cues(count: int, words_per_cue: int = 5, dur: float = 3.0) -> list[Cue]:
    out: list[Cue] = []
    for i in range(count):
        text = " ".join([f"w{i}_{k}" for k in range(words_per_cue)])
        out.append(Cue(start_sec=i * dur, end_sec=(i + 1) * dur, text=text))
    return out


def test_chunker_groups_cues_to_target_tokens():
    cues = _mk_cues(100, words_per_cue=10)
    chunks = Chunker(target_tokens=500).chunk(cues)

    assert len(chunks) >= 2
    for c in chunks:
        assert isinstance(c, Chunk)
        assert c.start_sec >= 0
        assert c.end_sec > c.start_sec

    assert [c.idx for c in chunks] == list(range(len(chunks)))


def test_chunker_empty_input():
    assert Chunker(target_tokens=500).chunk([]) == []


def test_chunker_single_short_cue():
    cues = [Cue(0.0, 1.0, "hello world")]
    chunks = Chunker(target_tokens=500).chunk(cues)
    assert len(chunks) == 1
    assert chunks[0].text == "hello world"
    assert chunks[0].start_sec == 0.0
    assert chunks[0].end_sec == 1.0


def test_chunker_preserves_total_word_count():
    cues = _mk_cues(50, words_per_cue=7)
    chunks = Chunker(target_tokens=300).chunk(cues)

    expected_words = sum(len(c.text.split()) for c in cues)
    got_words = sum(len(c.text.split()) for c in chunks)
    assert expected_words == got_words
