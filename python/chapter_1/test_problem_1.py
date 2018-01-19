import pytest
from python.chapter_1.problem_1 import unique_characters, unique_characters_no_cache


@pytest.mark.parametrize("text, result", [("abc", True), ("aac", False), ("aBbc", True)])
def test_character_uniqueness(text, result):
    assert unique_characters(text) == result


@pytest.mark.parametrize("text, result",  [("aca", False)])
def test_character_uniqueness(text, result):
    assert unique_characters_no_cache(text) == result
