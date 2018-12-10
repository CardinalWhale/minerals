import sqlite3
conn = sqlite3.connect('db.sqlite3')
print ("Opened database successfully")
f = open('d:/minerals/vitraj/txt/Imgminer.txt')
for line in f:
    print(line)
    p = line.split(';')
    t = p[0]
    n = p[1]
    sql = "insert into Vitraj_Imgminer (MId, Name) values (?, ?)"
    params = (t, n)
    conn.execute(sql, params)
    conn.commit()
f.close()
