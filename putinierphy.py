import sqlite3
conn = sqlite3.connect('db.sqlite3')
print ("Opened database successfully")
f = open('d:/minerals/vitraj/txt/Ierphysic.txt')
for line in f:
    print(line)
    p = line.split(';')
    t = p[0]
    n = p[1]
    r = p[2]
    sql = "insert into Vitraj_Ierphy (Type, Name, Razm) values (?, ?, ?)"
    params = (t, n, r)
    conn.execute(sql, params)
    conn.commit()
f.close()
