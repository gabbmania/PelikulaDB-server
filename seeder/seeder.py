import os

import requests
from dotenv import load_dotenv

load_dotenv()

MOVIE_URL = "https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=false&language=en-US&page=1&sort_by=popularity.desc"
GENRE_URL = "https://api.themoviedb.org/3/genre/movie/list?language=en"
HEADERS = {
    "accept": "application/json",
    "Authorization": f"Bearer {os.getenv('TMDB_API_KEY')}",
}


def fetch_data(url: str, key: str) -> list[dict]:
    response = requests.get(url, headers=HEADERS)
    return response.json()[key]


def convert_genre_id_to_name(all_genres: list[dict], genre_ids: list[int]) -> list[str]:
    return [
        genre["name"]
        for genre_id in genre_ids
        for genre in all_genres
        if genre_id == genre["id"]
    ]


def main() -> None:
    movies = fetch_data(MOVIE_URL, "results")
    all_genres = fetch_data(GENRE_URL, "genres")
    for movie in movies:
        title = movie["title"]
        overview = movie["overview"]
        genre_ids = movie["genre_ids"]
        release_date = movie["release_date"]
        language = movie["original_language"]
        poster_path = f"https://image.tmdb.org/t/p/original{movie['poster_path']}"

        movie_genre = convert_genre_id_to_name(all_genres, genre_ids)

        print(title)
        print(overview)
        print(movie_genre)
        print(release_date)
        print(language)
        print(poster_path)


if __name__ == "__main__":
    main()
