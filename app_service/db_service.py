import sqlite3


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


def find_text(con: sqlite3.Connection, text: str):
    con.row_factory = dict_factory
    return con.execute(f"""SELECT * 
        FROM subtitles 
        WHERE content LIKE '%{text}%';
        """).fetchall()


def get_text(con: sqlite3.Connection, text: str):
    res = find_text(con, text)
    # contents = [d['content'] for d in res]
    return res


if __name__ == '__main__':
    con = sqlite3.connect('HappyEnglishSubtitles.db')
    r = get_text(con, ' must ')
    print(*r, sep=' ')
    con.close()

