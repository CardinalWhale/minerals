import sqlite3
conn = sqlite3.connect('db.sqlite3')
print ("Opened database successfully")
f = open('d:/minerals/vitraj/txt/Imgminer.txt')
for line in f:
    p = line.split(';')
    nam = p[1]
    cura = conn.cursor()
    curb = conn.cursor()
    curc = conn.cursor()
    new = open('d:/minerals/vitraj/templates/vitraj/' +nam+ '.htm', 'w', encoding="utf-8")
    new.write("{% extends 'vitraj/base.html' %}\n")
    new.write('{% block title %}\n')
    new.write('Домой\n')
    new.write('{% endblock %}\n')
    new.write('{% block content %}\n')
    new.write('{% load static %}\n')
    new.write('<body>\n')
    new.write('<br />\n')
    new.write('<br />\n')
    new.write('<h1>')
    new.write(str('Свойства минерала {}'.format(nam)))
    new.write('</h1>\n')
    new.write('<img ')
    new.write('src="{% static "')
    new.write('media/images/vitraj/{}.jpg'.format(nam))
    new.write('"%}"')
    new.write('class="bw" width="250" height="250"')
    new.write(' alt="{}"'.format(nam))
    new.write('>\n')
    new.write('<h2>Химическая формула</h2>\n')
    sql = "select Formula from vitraj_chemform where Name = '%s'" % nam
    cura.execute(sql)
    result = cura.fetchall()
    ittt = 0
    for item in result:
        #new.write(str(item))
        iiittt = str(item)
        ll = len(iiittt)
        new.write('<h3>')
        new.write(iiittt[2:ll-3])
        new.write('</h3>\n')
    new.write('<h2>Химические свойства</h2>\n')
    sql = "select Inier, Val from vitraj_chemical where Name = '%s'" % nam
    cura.execute(sql)
    result = cura.fetchall()
    for item in result:
        ier=int(item[0])
        v=float(item[1])
        sql = "select Name, Abbr, Minmax, Razm from vitraj_ierchem where Type = '%i'" % ier
        curb.execute(sql)
        res = curb.fetchall()
        ititit = 0
        for it in res:
            n=(it[0])
            a = (it[1])
            m = (it[2])
            r = (it[3])
            if(v>0):
                new.write('<h3>')
                new.write('{} '.format(n))
                new.write('{} '.format(a))
                new.write('{} '.format(m))
                new.write('{} '.format(v))
                new.write('{} '.format(r))
                new.write('</h3>\n')
            if(v==0):
                if(ittt == 0):
                    new.write('<h3>')
                    new.write('Примесь:')
                    new.write('</h3>\n')
                    ittt=1          
                new.write('<p>')
                new.write('{} '.format(n))
                new.write('{} '.format(a))
                new.write('</p>\n')                
    new.write('<h2>Физические свойства</h2>\n')
    sql = "select Ier, Val from vitraj_physic where Name = '%s'" % nam
    cura.execute(sql)
    result = cura.fetchall()
    for item in result:
        #print (item)
        ier = float(item[0])
        val = float(item[1])
        sql = "select Name, Razm from vitraj_ierphy where Type = '%f'" % ier
        curb.execute(sql)
        res = curb.fetchall()
        for it in res:
            #print(it)
            i = (it[0])
            r =(it[1])
            if(val==0):
                ii = int(ier)
                iii = float(ii)
                sql = "select Name, Razm from vitraj_ierphy where Type = '%f'"  % iii
                curc.execute(sql)
                res1  = curc.fetchall()
                for iiii in res1:
                    iiiii = iiii[0]
                    ittt = iiii[1]
                    if(ii != ititit):
                        new.write('<h3>')
                        new.write('{} '.format(iiiii))
                        new.write('</h3>\n')
                        ititit = ii
                    new.write('<p>')
                    new.write('{}'.format(i))
                    new.write('</p>\n')
            if(val>0):
                new.write('<h3>')
                new.write('{} '.format(i))
                new.write('{} '.format(val))
                new.write('{} '.format(r))
                new.write('</h3>\n')
    new.write('<h2>Интерфейс</h2>\n')
    sql = "select Val from vitraj_interface where Name = '%s'" % nam
    cura.execute(sql)
    result = cura.fetchall()
    for item in result:
        #print (item)
        sql = "select Name from vitraj_ierin where Type = '%f'" % item
        curb.execute(sql)
        res = curb.fetchall()
        for it in res:
            iitt = str(it)
            ll = len(iitt)
            new.write('<h3>')
            l = len(str(item))-7
            if (l==1):
                new.write('Тип - ')
                new.write(iitt[2:ll-3])
                new.write('</h3>\n')
            elif (l==2):
                new.write('Класс - ')
                new.write(iitt[2:ll-3])
                new.write('</h3>\n')
            elif (l==3):
                new.write('Подкласс - ')
                new.write(iitt[2:ll-3])
                new.write('</h3>\n')                
            elif (l==4):
                new.write('Надотдел - ')
                new.write(iitt[2:ll-3])
                new.write('</h3>\n')                
            elif (l==5):
                new.write('Отдел - ')
                new.write(iitt[2:ll-3])
                new.write('</h3>\n')                
            elif (l==6):
                new.write('Подотдел - ')
                new.write(iitt[2:ll-3])
                new.write('</h3>\n')                
            elif (l==7):
                new.write('Семейство - ')
                new.write(iitt[2:ll-3])
                new.write('</h3>\n')                
            elif (l==8):
                new.write('Подсемейство - ')
                new.write(iitt[2:ll-3])
                new.write('</h3>\n')                
            elif (l==9):
                new.write('Группа - ')
                new.write(iitt[2:ll-3])
                new.write('</h3>\n')
            elif (l==10):
                new.write('Подгруппа - ')
                new.write(iitt[2:ll-3])
                new.write('</h3>\n')                
    new.write('</body>\n')
    new.write('{% endblock %}\n')
    cura.close()
    curb.close()
    new.close()
conn.close()
f.close()

