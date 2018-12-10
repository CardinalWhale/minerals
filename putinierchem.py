import sqlite3
conn = sqlite3.connect('db.sqlite3')
print ("Opened database successfully")
f = open('d:/minerals/vitraj/txt/Minierchem.txt')
for line in f:
    print(line)
    p = line.split(';')
    t = p[0]
    m = p[1]
    n = p[2]
    a = p[3]
    r = p[4]
    sql = "insert into Vitraj_Ierchem (Type, Minmax, Name, Abbr, Razm) values (?, ?, ?, ?, ?)"
    params = (t, m, n, a, r)
    conn.execute(sql, params)
    conn.commit()
f.close()