import sqlite3

conn= sqlite3.connect('emaildb.sqlite')
cur= conn.cursor()

cur.execute('DROP TABLE IF EXISTS user')

cur.execute('''
CREATE TABLE user (email TEXT, count INTEGER)''')

fname=input('Enter file name: ')
if (len(fname)<1): fname='mbox.txt'
fh=open(fname)
for line in fh:
    if not line.startswith('From: '): continue
    pieces=line.split()
    email= pieces[1]
    cur.execute('SELECT count FROM user WHERE email = ? ', (email,))
    row=cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO user (email, count)
                            VALUES (?,1)''', (email,))
    else:
        cur.execute('UPDATE user SET count = count + 1 WHERE email = ?',
                    (email,))
    conn.commit()
cur.close()

