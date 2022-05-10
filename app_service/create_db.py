import sqlite3
import sys


def create_db(path=None):
    if not path:
        path = '../HappyEnglishSubtitles.db'
    con = sqlite3.connect(path)
    cur = con.cursor()
    cur.execute('''CREATE TABLE if NOT EXISTS subtitles (
        video_id INTEGER
        , duration INTEGER 
        , content text
        , start_of_paragraph INTEGER 
        , start_time INTEGER 
        )''')
    cur.close()
    con.commit()
    con.close()


if __name__ == '__main__':
    path = sys.argv[1]
    create_db(path)
