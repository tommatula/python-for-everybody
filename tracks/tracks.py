import sqlite3
import os

fpath = os.path.dirname(__file__)
fname = fpath+'/tracks.csv'

conn = sqlite3.connect(fpath+'trackdb.sqlite')
cur = conn.cursor()

# Make some fresh tables using executescript()
cur.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;
DROP TABLE IF EXISTS Genre;

CREATE TABLE Artist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Genre (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title   TEXT UNIQUE
);

CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY 
        AUTOINCREMENT UNIQUE,
    title TEXT  UNIQUE,
    album_id  INTEGER,
    genre_id  INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
);
''')

handle = open(fname)

# Another One Bites The Dust,Queen,Greatest Hits,55,100,217103
#   0                          1      2           3  4   5

for line in handle:
    line = line.strip();
    pieces = line.split(',')
    if len(pieces) < 6 : continue

    name = pieces[0]
    artist = pieces[1]
    title = pieces[2]
    count1 = pieces[3]
    count2 = pieces[4]
    count3 = pieces[5]
    genre = pieces[6]

    #print(name, artist, album, genre)
    
    cur.execute('''INSERT OR IGNORE INTO Artist (name) 
        VALUES ( ? )''', ( artist, ) )
    cur.execute('SELECT id FROM Artist WHERE name = ? ', (artist,))
    artist_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Genre (name) 
        VALUES ( ? )''', ( genre, ) )
    cur.execute('SELECT id FROM Genre WHERE name = ? ', (genre,))
    genre_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Album (artist_id,title) 
        VALUES ( ?, ? )''', (artist_id,title) )
    cur.execute('SELECT id FROM Album WHERE title = ? ', (title,))
    album_id = cur.fetchone()[0]
    
    cur.execute('''INSERT OR IGNORE INTO Track (title, album_id, genre_id, len) 
        VALUES ( ?, ?, ?, ? )''', (title, album_id, genre_id,count1) )
    cur.execute('SELECT id FROM Album WHERE title = ? ', (title,))
    track_id = cur.fetchone()[0]

    conn.commit()
