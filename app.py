from __future__ import annotations

import os
from dataclasses import dataclass
from datetime import date
from urllib.parse import quote

from flask import Flask, render_template

app = Flask(__name__, static_folder="public/static", static_url_path="/static")


@dataclass(frozen=True)
class OpenPicture:
    title: str
    filename: str
    description: str
    artist: str
    license: str


PICTURES = [
    OpenPicture(
        title="The Great Wave off Kanagawa",
        filename="The_Great_Wave_off_Kanagawa.jpg",
        description="A public domain woodblock print by Katsushika Hokusai.",
        artist="Katsushika Hokusai",
        license="Public domain",
    ),
    OpenPicture(
        title="Earthrise",
        filename="NASA-Apollo8-Dec24-Earthrise.jpg",
        description="The Earth rising over the Moon, photographed during Apollo 8.",
        artist="NASA / Bill Anders",
        license="Public domain",
    ),
    OpenPicture(
        title="Hubble Ultra Deep Field",
        filename="Hubble_ultra_deep_field.jpg",
        description="A deep-space view captured by the Hubble Space Telescope.",
        artist="NASA, ESA, S. Beckwith and the HUDF Team",
        license="Public domain",
    ),
    OpenPicture(
        title="Ophelia",
        filename="John_Everett_Millais_-_Ophelia_-_Google_Art_Project.jpg",
        description="John Everett Millais' painting of Ophelia among flowers and water.",
        artist="John Everett Millais",
        license="Public domain",
    ),
    OpenPicture(
        title="Water Lilies",
        filename="Claude_Monet_-_Water_Lilies_-_Google_Art_Project.jpg",
        description="A quiet water garden scene painted by Claude Monet.",
        artist="Claude Monet",
        license="Public domain",
    ),
    OpenPicture(
        title="Wheat Field with Cypresses",
        filename="Vincent_van_Gogh_-_Wheat_Field_with_Cypresses_-_Google_Art_Project.jpg",
        description="A vivid landscape by Vincent van Gogh.",
        artist="Vincent van Gogh",
        license="Public domain",
    ),
    OpenPicture(
        title="The Blue Marble",
        filename="The_Blue_Marble_(remastered).jpg",
        description="A full view of Earth from the Apollo 17 mission.",
        artist="NASA",
        license="Public domain",
    ),
]


def format_display_date(day: date) -> str:
    return day.strftime("%B %d, %Y").replace(" 0", " ")


def picture_for(day: date) -> dict[str, str]:
    picture = PICTURES[day.toordinal() % len(PICTURES)]
    file_path = quote(picture.filename)

    return {
        "date": format_display_date(day),
        "title": picture.title,
        "description": picture.description,
        "image_url": f"https://commons.wikimedia.org/wiki/Special:FilePath/{file_path}",
        "file_page": f"https://commons.wikimedia.org/wiki/File:{file_path}",
        "artist": picture.artist,
        "license": picture.license,
        "license_url": "https://commons.wikimedia.org/wiki/Commons:Licensing",
    }


@app.get("/")
def home():
    picture = picture_for(date.today())
    return render_template("index.html", picture=picture)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", "5000"))
    app.run(host="127.0.0.1", port=port, debug=True)
