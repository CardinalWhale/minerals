import sqlite3
conn = sqlite3.connect('db.sqlite3')
print ("Opened database successfully")
f = open('d:/minerals/vitraj/txt/Mininter.txt')
for line in f:
    print(line)
    p = line.split(';')
    t = p[0]
    n = p[1]
    v = p[2]
    sql = "insert into Vitraj_Interface (MId, Name, Val) values (?, ?, ?)"
    params = (t, n, v)
    conn.execute(sql, params)
    conn.commit()
f.close()
