import os

import requests
from dotenv import load_dotenv

load_dotenv()

URL = "https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=false&language=en-US&page=1&sort_by=popularity.desc"
HEADERS = {
    "accept": "application/json",
    "Authorization": f"Bearer {os.getenv('TMDB_API_KEY')}",
}


def main() -> None:
    response = requests.get(URL, headers=HEADERS)
    print(response.text)


if __name__ == "__main__":
    main()
