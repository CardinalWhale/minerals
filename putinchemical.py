import sqlite3
conn = sqlite3.connect('db.sqlite3')
print ("Opened database successfully")
f = open('D:/minerals/vitraj/txt/Minchem.txt')
for line in f:
    print(line)
    p = line.split(';')
    t = p[0]
    n = p[1]
    i = p[2]
    v = p[3]
    sql = "insert into Vitraj_Chemical (MId, Name, Inier, Val) values (?, ?, ?, ?)"
    params = (t, n, i, v)
    conn.execute(sql, params)
    conn.commit()
f.close()
