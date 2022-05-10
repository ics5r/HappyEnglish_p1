import sqlite3
import sys
from urllib.request import urlopen
from urllib.error import HTTPError
from json import loads
from tqdm import tqdm


def get_ted_subtitles(video_id: int, lang: str) -> list[dict]:
    try:
        ted_url = urlopen(f'https://www.ted.com/talks/subtitles/id/{video_id}/lang/{lang}')
    except HTTPError as e:
        return None
    content_json = ted_url.read().decode('utf8')
    content = loads(content_json)
    rows = []
    for line in content['captions']:
        rows.append([video_id] + [value for name, value in line.items()])
    return rows


def upload_ted_subtitles(connection: sqlite3.Connection, start_id: int, end_id: int) -> None:
    cursor = connection.cursor()
    for video_id in tqdm(range(start_id, end_id)):
        rows = get_ted_subtitles(video_id, 'en')
        if not rows:
            continue
        cursor.executemany("INSERT INTO subtitles VALUES (?, ?, ?, ?, ?)", rows)
    cursor.close()
    connection.commit()
    return


def fill_db(start=1, finish=100, path='../HappyEnglishSubtitles.db'):
    con = sqlite3.connect(path)
    upload_ted_subtitles(con, start, finish)


if __name__ == '__main__':
    path = sys.argv[1]
    # path = 'HappyEnglishSubtitles.db'
    con = sqlite3.connect(path)
    upload_ted_subtitles(con, 1, 100)
    con.close()
