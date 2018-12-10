import sqlite3
conn = sqlite3.connect('db.sqlite3')
print("Opened database successfully")
f = open('d:/minerals/vitraj/txt/Minchemform.txt')
for line in f:
    print(line)
    p = line.split(';')
    t = p[0]
    n = p[1]
    f = p[2]
    sql = "insert into Vitraj_Chemform(MId, Name, Formula) values (?, ?, ?)"
    params = (t, n, f)
    conn.execute(sql, params)
    conn.commit()
f.close()