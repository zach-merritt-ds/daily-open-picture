from datetime import date

from app import PICTURES, format_display_date, picture_for


def test_format_display_date_removes_leading_day_zero():
    assert format_display_date(date(2026, 5, 3)) == "May 3, 2026"


def test_format_display_date_keeps_two_digit_day():
    assert format_display_date(date(2026, 5, 23)) == "May 23, 2026"


def test_picture_for_returns_a_curated_open_picture():
    picture = picture_for(date(2026, 5, 23))

    assert picture["title"]
    assert picture["image_url"].startswith("https://commons.wikimedia.org/wiki/Special:FilePath/")
    assert picture["license"] in {"Public domain", "CC0"}
    assert len(PICTURES) >= 7
