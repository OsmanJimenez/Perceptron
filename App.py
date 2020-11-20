from flask import Flask, render_template
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'perceptron'
mysql = MySQL(app)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/and')
def cand():
    import random

    def calculo(t, e, um, x1, x2, d, p1, p2, u, n, pat):
        
        y = ( p1 * x1) + (p2 * x2) - u
        f = 0
        e = 0
        
        if y >= 0:
            f = 1
        elif y < 0:
            f = 0
        else:
            print("Hay un problema al calcular el coeficiente de aprendizaje (y)") 
            
        e = d - f
        
        v1 = n * e * x1
        v2 = n * e * x2
        
        pe1 = p1 + v1 
        pe2 = p2 + v2

        um = round( (u - (n * e)) , 2)

        print("\n", 
            "################################","\n","Iteración ", t,"\n", "################################","\n","patron:",pat,"\n","x1:",x1,"\n", "x2:",x2,"\n","p1:",p1,"\n","p2:",p2,"\n","n:",n,"\n","y:",y,"\n","f:",f,"\n","d:",d,"\n","u:",u,"\n","e:",e,"\n","v1:",v1,"\n","v2:",v2,"\n","pe1:",pe1,"\n","pe2:",pe2,"\n","um:",um,"\n",)
        cur = mysql.connection.cursor()
        
        cur.execute('INSERT INTO compuerta_an (Patron, x1, x2, p1, p2,u,d, y, fx,n,e,v1,v2,pe1,pe2,um,it) VALUES (%s, %s, %s, %s, %s,%s,%s, %s, %s,%s,%s,%s,%s,%s,%s,%s,%s)',
        (pat, x1, x2, p1, p2,u,d, y, f,n,e,v1,v2,pe1,pe2,um,t))
        
        mysql.connection.commit()
        
        t += 1
        um_lis.append(um)
        
        
        
        return (t,  e, um)

    def valor_espe(d, pat, x1, x2):
        if x1== 0 and x2==0:
            d = 0
            pat = 1
        elif x1== 0 and x2==1:
            d = 0
            pat = 2
        elif x1== 1 and x2==0:
            d = 0
            pat = 3
        elif x1== 1 and x2==1:
            d = 1
            pat = 4
        else:
            print("Error en los pesos, valores deben ser 1 o 0")
        return(d, pat)

    def pesos(p1, p2, u):
        p1 = round(random.uniform(-1.0, 1.0), 2)
        p2 = round(random.uniform(-1.0, 1.0), 2)
        u = round(random.uniform(-1.0, 1.0), 2)
        return (p1, p2, u)

    t = 1
    d = 0
    e = 2
    p1 = 0
    p2 = 0
    u = 0
    p1 ,p2 , u = pesos(p1, p2, u)
    um_lis = [0, 0, 0, 1]
    um = 1
    n = round(random.uniform(0, 1.0), 2)
    pat = 0
    
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM compuerta_an ')
    mysql.connection.commit()

    while um_lis[-1] != um or um_lis[-2] != um or um_lis[-3] != um or um_lis[-4] != um :
        for i in [0, 1, ]:
            for j in [0, 1]:
                            
                x1=i
                x2=j
                
                if um_lis[-1] == um and um_lis[-2] == um and um_lis[-3] == um and um_lis[-4] == um :
                    break       
                elif e == 0:
                    d, pat = valor_espe(d, pat, x1, x2)             
                    t, e, um = calculo(t, e, um, x1, x2, d, p1, p2, u, n, pat)
                    if e != 0 :
                        p1 ,p2 , u = pesos(p1, p2, u)
                        d, pat = valor_espe(d, pat, x1, x2)             
                        t, e, um = calculo(t, e, um, x1, x2, d, p1, p2, u, n, pat)
                else:
                    while e != 0 :
                        p1 ,p2 , u = pesos(p1, p2, u)
                        d, pat = valor_espe(d, pat, x1, x2)             
                        t, e, um = calculo(t, e, um, x1, x2, d, p1, p2, u, n, pat)
                    
                    
                        
                
    print(um)
    print(um_lis, "\n")
           
    
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM compuerta_an')    
    data = cur.fetchall()    
    
    cur2 = mysql.connection.cursor()
    cur2.execute('SELECT * FROM compuerta_an ORDER BY it DESC LIMIT 1')
    data2 = cur2.fetchall()
    
    cur3 = mysql.connection.cursor()
    cur3.execute('SELECT Patron, x1, x2, d FROM compuerta_an ORDER BY it DESC, Patron ASC LIMIT 4')
    data3 = cur3.fetchall()
    return render_template('and.html', compu_and = data, compu_and2 = data2[0], compu_and3 = data3)

@app.route('/and2')
def can3():
    import random

    def calculo(t, e, um, x1, x2, x3, d, p1, p2, p3, u, n, pat):
        y = round(( ( p1 * x1) + (p2 * x2) + (p3 * x3) - u ) , 2)
        f = 0
        e = 0
        
        if y >= 0:
            f = 1
        elif y < 0:
            f = 0
        else:
            print("Hay un problema al calcular el coeficiente de aprendizaje (y)") 
              
        e = d - f
        
        v1 = n * e * x1
        v2 = n * e * x2
        v3 = n * e * x3
        
        pe1 = p1 + v1 
        pe2 = p2 + v2
        pe3 = p3 + v3


        um = round( (u - (n * e)) , 2)

        print("\n", 
            "################################","\n","Iteración ", t,"\n", "################################","\n","patron:",pat,"\n","x1:",x1,"\n", "x2:",x2,"\n", "x3:",x3,"\n","p1:",p1,"\n","p2:",p2,"\n","p3:",p3,"\n","n:",n,"\n","y:",y,"\n","f:",f,"\n","d:",d,"\n","u:",u,"\n","e:",e,"\n","v1:",v1,"\n","v2:",v2,"\n","v3:",v3,"\n","pe1:",pe1,"\n","pe2:",pe2,"\n","pe3:",pe3,"\n","um:",um,"\n",)
        cur = mysql.connection.cursor()
        
        cur.execute('INSERT INTO compuerta_an2 (Patron, x1, x2,x3, p1, p2,p3,u,d, y, fx,n,e,v1,v2,v3,pe1,pe2,pe3,um,it) VALUES (%s, %s, %s,%s,%s, %s, %s, %s, %s,%s,%s, %s, %s,%s,%s,%s,%s,%s,%s,%s,%s)',
        (pat, x1, x2,x3, p1, p2,p3,u,d, y, f,n,e,v1,v2,v3,pe1,pe2,pe3,um,t))

        mysql.connection.commit()

        t += 1
        um_lis.append(um)
        return (t,  e, um)

    def valor_espe(d, pat, x1, x2, x3):
        if x1== 0 and x2==0 and x3==0:
            d = 0
            pat = 1
        elif x1== 0 and x2==0 and x3==1:
            d = 0
            pat = 2
        elif x1== 0 and x2==1 and x3==0:
            d = 0
            pat = 3
        elif x1== 0 and x2==1 and x3==1:
            d = 0
            pat = 4
        elif x1== 1 and x2==0 and x3==0:
            d = 0
            pat = 5
        elif x1== 1 and x2==0 and x3==1:
            d = 0
            pat = 6
        elif x1== 1 and x2==1 and x3==0:
            d = 0
            pat = 7
        elif x1== 1 and x2==1 and x3==1:
            d = 1
            pat = 8
        else:
            print("Error en los pesos, valores deben ser 1 o 0")
        return(d, pat)

    def pesos(p1, p2, p3, u):
        p1 = round(random.uniform(-1.0, 1.0), 2)
        p2 = round(random.uniform(-1.0, 1.0), 2)
        p3 = round(random.uniform(-1.0, 1.0), 2)
        u = round(random.uniform(-1.0, 1.0), 2)
        return (p1, p2, p3, u)


    t = 1
    d = 0
    e = 1
    p1 = 0
    p2 = 0
    p3 = 0
    u = 0
    p1 ,p2 ,p3 , u = pesos(p1, p2, p3, u)
    um_lis = [0, 0, 0, 0, 0, 0, 0, 1]
    um = 1
    pat = 0

    n = round(random.uniform(0, 1.0), 2)

    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM compuerta_an2 ')
    mysql.connection.commit()

    while um_lis[-1] != um or um_lis[-2] != um or um_lis[-3] != um or um_lis[-4] != um or um_lis[-5] != um or um_lis[-6] != um or um_lis[-7] != um or um_lis[-8] != um:
        for i in [0, 1, ]:
            for j in [0, 1]:
                for k in [0, 1]:            
                    x1=i
                    x2=j 
                    x3=k 
                    
                    if um_lis[-1] == um and um_lis[-2] == um and um_lis[-3] == um and um_lis[-4] == um and um_lis[-5] == um and um_lis[-6] == um and um_lis[-7] == um and um_lis[-8] == um:
                            break       
                    elif e == 0:
                        d, pat = valor_espe(d, pat, x1, x2, x3)             
                        t, e, um = calculo(t, e, um, x1, x2, x3, d, p1, p2, p3, u, n, pat)
                        if e != 0 :
                            p1 ,p2 ,p3 , u = pesos(p1, p2, p3, u)
                            d, pat = valor_espe(d, pat, x1, x2, x3)             
                            t, e, um = calculo(t, e, um, x1, x2, x3, d, p1, p2, p3, u, n, pat)
                    else:
                        while e != 0 :
                            p1 ,p2 ,p3 , u = pesos(p1, p2, p3, u)
                            d, pat = valor_espe(d, pat, x1, x2, x3)             
                            t, e, um = calculo(t, e, um, x1, x2, x3, d, p1, p2, p3, u, n, pat)
                        
                
    print(um)
    print(um_lis, "\n")
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM compuerta_an2')    
    data = cur.fetchall()    
    
    cur2 = mysql.connection.cursor()
    cur2.execute('SELECT * FROM compuerta_an2 ORDER BY it DESC LIMIT 1')
    data2 = cur2.fetchall()
    
    cur3 = mysql.connection.cursor()
    cur3.execute('SELECT Patron, x1, x2,x3, d FROM compuerta_an2 ORDER BY it DESC, Patron ASC LIMIT 8')
    data3 = cur3.fetchall()
    return render_template('and2.html', compu_and = data, compu_and2 = data2[0], compu_and3 = data3)            

@app.route('/or')
def cand2():
    import random

    def calculo(t, e, um, x1, x2, d, p1, p2, u, n, pat):
        
        y = ( p1 * x1) + (p2 * x2) - u
        f = 0
        e = 0
        
        if y >= 0:
            f = 1
        elif y < 0:
            f = 0
        else:
            print("Hay un problema al calcular el coeficiente de aprendizaje (y)") 
            
        e = d - f
        
        v1 = n * e * x1
        v2 = n * e * x2
        
        pe1 = p1 + v1 
        pe2 = p2 + v2

        um = round( (u - (n * e)) , 2)

        print("\n", 
            "################################","\n","Iteración ", t,"\n", "################################","\n","patron:",pat,"\n","x1:",x1,"\n", "x2:",x2,"\n","p1:",p1,"\n","p2:",p2,"\n","n:",n,"\n","y:",y,"\n","f:",f,"\n","d:",d,"\n","u:",u,"\n","e:",e,"\n","v1:",v1,"\n","v2:",v2,"\n","pe1:",pe1,"\n","pe2:",pe2,"\n","um:",um,"\n",)
        cur = mysql.connection.cursor()
        
        cur.execute('INSERT INTO compuerta_or (Patron, x1, x2, p1, p2,u,d, y, fx,n,e,v1,v2,pe1,pe2,um,it) VALUES (%s, %s, %s, %s, %s,%s,%s, %s, %s,%s,%s,%s,%s,%s,%s,%s,%s)',
        (pat, x1, x2, p1, p2,u,d, y, f,n,e,v1,v2,pe1,pe2,um,t))
        
        mysql.connection.commit()
        
        t += 1
        um_lis.append(um)
        
        
        
        return (t,  e, um)

    def valor_espe(d, pat, x1, x2):
        if x1== 0 and x2==0:
            d = 0
            pat = 1
        elif x1== 0 and x2==1:
            d = 1
            pat = 2
        elif x1== 1 and x2==0:
            d = 1
            pat = 3
        elif x1== 1 and x2==1:
            d = 1
            pat = 4
        else:
            print("Error en los pesos, valores deben ser 1 o 0")
        return(d, pat)

    def pesos(p1, p2, u):
        p1 = round(random.uniform(-1.0, 1.0), 2)
        p2 = round(random.uniform(-1.0, 1.0), 2)
        u = round(random.uniform(-1.0, 1.0), 2)
        return (p1, p2, u)

    t = 1
    d = 0
    e = 2
    p1 = 0
    p2 = 0
    u = 0
    p1 ,p2 , u = pesos(p1, p2, u)
    um_lis = [0, 0, 0, 1]
    um = 1
    n = round(random.uniform(0, 1.0), 2)
    pat = 0
    
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM compuerta_or ')
    mysql.connection.commit()

    while um_lis[-1] != um or um_lis[-2] != um or um_lis[-3] != um or um_lis[-4] != um :
        for i in [0, 1, ]:
            for j in [0, 1]:
                            
                x1=i
                x2=j
                
                if um_lis[-1] == um and um_lis[-2] == um and um_lis[-3] == um and um_lis[-4] == um :
                    break       
                elif e == 0:
                    d, pat = valor_espe(d, pat, x1, x2)             
                    t, e, um = calculo(t, e, um, x1, x2, d, p1, p2, u, n, pat)
                    if e != 0 :
                        p1 ,p2 , u = pesos(p1, p2, u)
                        d, pat = valor_espe(d, pat, x1, x2)             
                        t, e, um = calculo(t, e, um, x1, x2, d, p1, p2, u, n, pat)
                else:
                    while e != 0 :
                        p1 ,p2 , u = pesos(p1, p2, u)
                        d, pat = valor_espe(d, pat, x1, x2)             
                        t, e, um = calculo(t, e, um, x1, x2, d, p1, p2, u, n, pat)
                    
                    
                        
                
    print(um)
    print(um_lis, "\n")
           
    
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM compuerta_or')    
    data = cur.fetchall()    
    
    cur2 = mysql.connection.cursor()
    cur2.execute('SELECT * FROM compuerta_or ORDER BY it DESC LIMIT 1')
    data2 = cur2.fetchall()
    
    cur3 = mysql.connection.cursor()
    cur3.execute('SELECT Patron, x1, x2, d FROM compuerta_or ORDER BY it DESC, Patron ASC LIMIT 4')
    data3 = cur3.fetchall()
    return render_template('or.html', compu_or = data, compu_or2 = data2[0], compu_or3 = data3)

@app.route('/or2')
def can4():
    import random

    def calculo(t, e, um, x1, x2, x3, d, p1, p2, p3, u, n, pat):
        y = round(( ( p1 * x1) + (p2 * x2) + (p3 * x3) - u ) , 2)
        f = 0
        e = 0
        
        if y >= 0:
            f = 1
        elif y < 0:
            f = 0
        else:
            print("Hay un problema al calcular el coeficiente de aprendizaje (y)") 
              
        e = d - f
        
        v1 = n * e * x1
        v2 = n * e * x2
        v3 = n * e * x3
        
        pe1 = p1 + v1 
        pe2 = p2 + v2
        pe3 = p3 + v3

        um = round( (u - (n * e)) , 2)

        print("\n", 
            "################################","\n","Iteración ", t,"\n", "################################","\n","patron:",pat,"\n","x1:",x1,"\n", "x2:",x2,"\n", "x3:",x3,"\n","p1:",p1,"\n","p2:",p2,"\n","p3:",p3,"\n","n:",n,"\n","y:",y,"\n","f:",f,"\n","d:",d,"\n","u:",u,"\n","e:",e,"\n","v1:",v1,"\n","v2:",v2,"\n","v3:",v3,"\n","pe1:",pe1,"\n","pe2:",pe2,"\n","pe3:",pe3,"\n","um:",um,"\n",)
        cur = mysql.connection.cursor()
        
        cur.execute('INSERT INTO compuerta_or2 (Patron, x1, x2,x3, p1, p2,p3,u,d, y, fx,n,e,v1,v2,v3,pe1,pe2,pe3,um,it) VALUES (%s, %s, %s,%s,%s, %s, %s, %s, %s,%s,%s, %s, %s,%s,%s,%s,%s,%s,%s,%s,%s)',
        (pat, x1, x2,x3, p1, p2,p3,u,d, y, f,n,e,v1,v2,v3,pe1,pe2,pe3,um,t))

        mysql.connection.commit()
        t += 1
        um_lis.append(um)
        return (t,  e, um)

    def valor_espe(d, pat, x1, x2, x3):
        if x1== 0 and x2==0 and x3==0:
            d = 0
            pat = 1
        elif x1== 0 and x2==0 and x3==1:
            d = 1
            pat = 2
        elif x1== 0 and x2==1 and x3==0:
            d = 1
            pat = 3
        elif x1== 0 and x2==1 and x3==1:
            d = 1
            pat = 4
        elif x1== 1 and x2==0 and x3==0:
            d = 1
            pat = 5
        elif x1== 1 and x2==0 and x3==1:
            d = 1
            pat = 6
        elif x1== 1 and x2==1 and x3==0:
            d = 1
            pat = 7
        elif x1== 1 and x2==1 and x3==1:
            d = 1
            pat = 8
        else:
            print("Error en los pesos, valores deben ser 1 o 0")
        return(d, pat)

    def pesos(p1, p2, p3, u):
        p1 = round(random.uniform(-1.0, 1.0), 2)
        p2 = round(random.uniform(-1.0, 1.0), 2)
        p3 = round(random.uniform(-1.0, 1.0), 2)
        u = round(random.uniform(-1.0, 1.0), 2)
        return (p1, p2, p3, u)


    t = 1
    d = 0
    e = 1
    p1 = 0
    p2 = 0
    p3 = 0
    u = 0
    p1 ,p2 ,p3 , u = pesos(p1, p2, p3, u)
    um_lis = [0, 0, 0, 0, 0, 0, 0, 1]
    um = 1
    pat = 0

    n = round(random.uniform(0, 1.0), 2)

    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM compuerta_or2')
    mysql.connection.commit()

    while um_lis[-1] != um or um_lis[-2] != um or um_lis[-3] != um or um_lis[-4] != um or um_lis[-5] != um or um_lis[-6] != um or um_lis[-7] != um or um_lis[-8] != um:
        for i in [0, 1, ]:
            for j in [0, 1]:
                for k in [0, 1]:            
                    x1=i
                    x2=j 
                    x3=k 
                    
                    if um_lis[-1] == um and um_lis[-2] == um and um_lis[-3] == um and um_lis[-4] == um and um_lis[-5] == um and um_lis[-6] == um and um_lis[-7] == um and um_lis[-8] == um:
                            break       
                    elif e == 0:
                        d, pat = valor_espe(d, pat, x1, x2, x3)             
                        t, e, um = calculo(t, e, um, x1, x2, x3, d, p1, p2, p3, u, n, pat)
                        if e != 0 :
                            p1 ,p2 ,p3 , u = pesos(p1, p2, p3, u)
                            d, pat = valor_espe(d, pat, x1, x2, x3)             
                            t, e, um = calculo(t, e, um, x1, x2, x3, d, p1, p2, p3, u, n, pat)
                    else:
                        while e != 0 :
                            p1 ,p2 ,p3 , u = pesos(p1, p2, p3, u)
                            d, pat = valor_espe(d, pat, x1, x2, x3)             
                            t, e, um = calculo(t, e, um, x1, x2, x3, d, p1, p2, p3, u, n, pat)
                        
                
    print(um)
    print(um_lis, "\n")

    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM compuerta_or2')    
    data = cur.fetchall()    
    
    cur2 = mysql.connection.cursor()
    cur2.execute('SELECT * FROM compuerta_or2 ORDER BY it DESC LIMIT 1')
    data2 = cur2.fetchall()
    
    cur3 = mysql.connection.cursor()
    cur3.execute('SELECT Patron, x1, x2,x3, d FROM compuerta_or2 ORDER BY it DESC, Patron ASC LIMIT 8')
    data3 = cur3.fetchall()
    return render_template('or2.html', compu_or = data, compu_or2 = data2[0], compu_or3 = data3)
@app.route('/nor')
def can5():
    import random

    def calculo(t, e, um, x1, x2, d, p1, p2, u, n, pat):
        y = round(( ( p1 * x1) + (p2 * x2) - u) , 2)
        f = 0
        e = 0
        
        if y >= 0:
            f = 1
        elif y < 0:
            f = 0
        else:
            print("Hay un problema al calcular el coeficiente de aprendizaje (y)") 
              
        e = d - f
        
        v1 = n * e * x1
        v2 = n * e * x2
        
        pe1 = p1 + v1 
        pe2 = p2 + v2

        um = round( (u - (n * e)) , 2)

        print("\n", 
            "################################","\n","Iteración ", t,"\n", "################################","\n","patron:",pat,"\n","x1:",x1,"\n", "x2:",x2,"\n","p1:",p1,"\n","p2:",p2,"\n","n:",n,"\n","y:",y,"\n","f:",f,"\n","d:",d,"\n","u:",u,"\n","e:",e,"\n","v1:",v1,"\n","v2:",v2,"\n","pe1:",pe1,"\n","pe2:",pe2,"\n","um:",um,"\n",)
        cur = mysql.connection.cursor()
        
        cur.execute('INSERT INTO compuerta_nor (Patron, x1, x2, p1, p2,u,d, y, fx,n,e,v1,v2,pe1,pe2,um,it) VALUES ( %s, %s, %s, %s, %s,%s,%s, %s, %s,%s,%s,%s,%s,%s,%s,%s,%s)',
        (pat, x1, x2, p1, p2,u,d, y, f,n,e,v1,v2,pe1,pe2,um,t))

        mysql.connection.commit()
        t += 1
        um_lis.append(um)
        return (t,  e, um)

    def valor_espe(d, pat, x1, x2):
        if x1== 0 and x2==0:
            d = 1
            pat = 1
        elif x1== 0 and x2==1:
            d = 0
            pat = 2
        elif x1== 1 and x2==0:
            d = 0
            pat = 3
        elif x1== 1 and x2==1:
            d = 0
            pat = 4
        else:
            print("Error en los pesos, valores deben ser 1 o 0")
        return(d, pat)

    def pesos(p1, p2, u):
        p1 = round(random.uniform(-1.0, 1.0), 2)
        p2 = round(random.uniform(-1.0, 1.0), 2)
        u = round(random.uniform(-1.0, 1.0), 2)
        return (p1, p2, u)

    t = 1
    d = 0
    e = 1
    p1 = 0
    p2 = 0
    u = 0
    p1 ,p2 , u = pesos(p1, p2, u)
    um_lis = [0, 0, 0, 1]
    um = 1
    pat = 0

    n = round(random.uniform(0, 1.0), 2)

    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM compuerta_nor')
    mysql.connection.commit()

    while um_lis[-1] != um or um_lis[-2] != um or um_lis[-3] != um or um_lis[-4] != um :
        for i in [0, 1, ]:
            for j in [0, 1]:
                            
                x1=i
                x2=j  
                
                if um_lis[-1] == um and um_lis[-2] == um and um_lis[-3] == um and um_lis[-4] == um :
                        break       
                elif e == 0:
                    d, pat = valor_espe(d, pat, x1, x2)             
                    t, e, um = calculo(t, e, um, x1, x2, d, p1, p2, u, n, pat)
                    if e != 0 :
                        p1 ,p2 , u = pesos(p1, p2, u)
                        d, pat = valor_espe(d, pat, x1, x2)             
                        t, e, um = calculo(t, e, um, x1, x2, d, p1, p2, u, n, pat)
                else:
                    while e != 0 :
                        p1 ,p2 , u = pesos(p1, p2, u)
                        d, pat = valor_espe(d, pat, x1, x2)             
                        t, e, um = calculo(t, e, um, x1, x2, d, p1, p2, u, n, pat)
                        
                
    print(um)
    print(um_lis, "\n")
            

    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM compuerta_nor')    
    data = cur.fetchall()    
    
    cur2 = mysql.connection.cursor()
    cur2.execute('SELECT * FROM compuerta_nor ORDER BY it DESC LIMIT 1')
    data2 = cur2.fetchall()
    
    cur3 = mysql.connection.cursor()
    cur3.execute('SELECT Patron, x1, x2, d FROM compuerta_nor ORDER BY it DESC, Patron ASC LIMIT 4')
    data3 = cur3.fetchall()
    return render_template('nor.html', compu_nor = data, compu_nor2 = data2[0], compu_nor3 = data3)
@app.route('/nor2')
def can6():
    import random

    def calculo(t, e, um, x1, x2, x3, d, p1, p2, p3, u, n, pat):
        y = round(( ( p1 * x1) + (p2 * x2) + (p3 * x3) - u ) , 2)
        f = 0
        e = 0
        
        if y >= 0:
            f = 1
        elif y < 0:
            f = 0
        else:
            print("Hay un problema al calcular el coeficiente de aprendizaje (y)") 
              
        e = d - f
        
        v1 = n * e * x1
        v2 = n * e * x2
        v3 = n * e * x3
        
        pe1 = p1 + v1 
        pe2 = p2 + v2
        pe3 = p3 + v3

        um = round( (u - (n * e)) , 2)

        print("\n", 
            "################################","\n","Iteración ", t,"\n", "################################","\n","patron:",pat,"\n","x1:",x1,"\n", "x2:",x2,"\n", "x3:",x3,"\n","p1:",p1,"\n","p2:",p2,"\n","p3:",p3,"\n","n:",n,"\n","y:",y,"\n","f:",f,"\n","d:",d,"\n","u:",u,"\n","e:",e,"\n","v1:",v1,"\n","v2:",v2,"\n","v3:",v3,"\n","pe1:",pe1,"\n","pe2:",pe2,"\n","pe3:",pe3,"\n","um:",um,"\n",)
        cur = mysql.connection.cursor()
        
        cur.execute('INSERT INTO compuerta_nor2 (Patron, x1, x2,x3, p1, p2,p3,u,d, y, fx,n,e,v1,v2,v3,pe1,pe2,pe3,um,it) VALUES (%s, %s, %s,%s,%s, %s, %s,%s,%s, %s, %s, %s, %s,%s,%s, %s, %s,%s,%s,%s,%s)',
        (pat, x1, x2,x3, p1, p2,p3,u,d, y, f,n,e,v1,v2,v3,pe1,pe2,pe3,um,t))

        mysql.connection.commit()
        t += 1
        um_lis.append(um)
        return (t,  e, um)

    def valor_espe(d, pat, x1, x2, x3):
        if x1== 0 and x2==0 and x3==0:
            d = 1
            pat = 1
        elif x1== 0 and x2==0 and x3==1:
            d = 0
            pat = 2
        elif x1== 0 and x2==1 and x3==0:
            d = 0
            pat = 3
        elif x1== 0 and x2==1 and x3==1:
            d = 0
            pat = 4
        elif x1== 1 and x2==0 and x3==0:
            d = 0
            pat = 5
        elif x1== 1 and x2==0 and x3==1:
            d = 0
            pat = 6
        elif x1== 1 and x2==1 and x3==0:
            d = 0
            pat = 7
        elif x1== 1 and x2==1 and x3==1:
            d = 0
            pat = 8
        else:
            print("Error en los pesos, valores deben ser 1 o 0")
        return(d, pat)

    def pesos(p1, p2, p3, u):
        p1 = round(random.uniform(-1.0, 1.0), 2)
        p2 = round(random.uniform(-1.0, 1.0), 2)
        p3 = round(random.uniform(-1.0, 1.0), 2)
        u = round(random.uniform(-1.0, 1.0), 2)
        return (p1, p2, p3, u)


    t = 1
    d = 0
    e = 1
    p1 = 0
    p2 = 0
    p3 = 0
    u = 0
    p1 ,p2 ,p3 , u = pesos(p1, p2, p3, u)
    um_lis = [0, 0, 0, 0, 0, 0, 0, 1]
    um = 1
    pat = 0

    n = round(random.uniform(0, 1.0), 2)

    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM compuerta_nor2')
    mysql.connection.commit()

    while um_lis[-1] != um or um_lis[-2] != um or um_lis[-3] != um or um_lis[-4] != um or um_lis[-5] != um or um_lis[-6] != um or um_lis[-7] != um or um_lis[-8] != um:
        for i in [0, 1, ]:
            for j in [0, 1]:
                for k in [0, 1]:            
                    x1=i
                    x2=j 
                    x3=k 
                    
                    if um_lis[-1] == um and um_lis[-2] == um and um_lis[-3] == um and um_lis[-4] == um and um_lis[-5] == um and um_lis[-6] == um and um_lis[-7] == um and um_lis[-8] == um:
                            break       
                    elif e == 0:
                        d, pat = valor_espe(d, pat, x1, x2, x3)             
                        t, e, um = calculo(t, e, um, x1, x2, x3, d, p1, p2, p3, u, n, pat)
                        if e != 0 :
                            p1 ,p2 ,p3 , u = pesos(p1, p2, p3, u)
                            d, pat = valor_espe(d, pat, x1, x2, x3)             
                            t, e, um = calculo(t, e, um, x1, x2, x3, d, p1, p2, p3, u, n, pat)
                    else:
                        while e != 0 :
                            p1 ,p2 ,p3 , u = pesos(p1, p2, p3, u)
                            d, pat = valor_espe(d, pat, x1, x2, x3)             
                            t, e, um = calculo(t, e, um, x1, x2, x3, d, p1, p2, p3, u, n, pat)
                        
                
    print(um)
    print(um_lis, "\n")
        

    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM compuerta_nor2')    
    data = cur.fetchall()    
    
    cur2 = mysql.connection.cursor()
    cur2.execute('SELECT * FROM compuerta_nor2 ORDER BY it DESC LIMIT 1')
    data2 = cur2.fetchall()
    
    cur3 = mysql.connection.cursor()
    cur3.execute('SELECT Patron, x1, x2,x3, d FROM compuerta_nor2 ORDER BY it DESC, Patron ASC LIMIT 8')
    data3 = cur3.fetchall()
    return render_template('nor2.html', compu_nor = data, compu_nor2 = data2[0], compu_nor3 = data3)        
@app.route('/nan')
def can7():
    import random

    def calculo(t, e, um, x1, x2, d, p1, p2, u, n, pat):
        y = round(( ( p1 * x1) + (p2 * x2) - u) , 2)
        f = 0
        e = 0
        
        if y >= 0:
            f = 1
        elif y < 0:
            f = 0
        else:
            print("Hay un problema al calcular el coeficiente de aprendizaje (y)") 
              
        e = d - f
        
        v1 = n * e * x1
        v2 = n * e * x2
        
        pe1 = p1 + v1 
        pe2 = p2 + v2

        um = round( (u - (n * e)) , 2)

        print("\n", 
            "################################","\n","Iteración ", t,"\n", "################################","\n","patron:",pat,"\n","x1:",x1,"\n", "x2:",x2,"\n","p1:",p1,"\n","p2:",p2,"\n","n:",n,"\n","y:",y,"\n","f:",f,"\n","d:",d,"\n","u:",u,"\n","e:",e,"\n","v1:",v1,"\n","v2:",v2,"\n","pe1:",pe1,"\n","pe2:",pe2,"\n","um:",um,"\n",)
        
        cur.execute('INSERT INTO compuerta_nan (Patron, x1, x2, p1, p2,u,d, y, fx,n,e,v1,v2,pe1,pe2,um,it) VALUES (%s,%s, %s, %s,%s,%s, %s, %s, %s, %s,%s,%s, %s, %s,%s, %s, %s)',
        (pat, x1, x2, p1, p2,u,d, y, f,n,e,v1,v2,pe1,pe2,um,t))

        mysql.connection.commit()

        t += 1
        um_lis.append(um)
        return (t,  e, um)

    def valor_espe(d, pat, x1, x2):
        if x1== 0 and x2==0:
            d = 1
            pat = 1
        elif x1== 0 and x2==1:
            d = 1
            pat = 2
        elif x1== 1 and x2==0:
            d = 1
            pat = 3
        elif x1== 1 and x2==1:
            d = 0
            pat = 4
        else:
            print("Error en los pesos, valores deben ser 1 o 0")
        return(d, pat)

    def pesos(p1, p2, u):
        p1 = round(random.uniform(-1.0, 1.0), 2)
        p2 = round(random.uniform(-1.0, 1.0), 2)
        u = round(random.uniform(-1.0, 1.0), 2)
        return (p1, p2, u)

    t = 1
    d = 0
    e = 1
    p1 = 0
    p2 = 0
    u = 0
    p1 ,p2 , u = pesos(p1, p2, u)
    um_lis = [0, 0, 0, 1]
    um = 1
    pat = 0

    n = round(random.uniform(0, 1.0), 2)

    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM compuerta_nan')
    mysql.connection.commit()

    while um_lis[-1] != um or um_lis[-2] != um or um_lis[-3] != um or um_lis[-4] != um :
        for i in [0, 1, ]:
            for j in [0, 1]:
                            
                x1=i
                x2=j  
                
                if um_lis[-1] == um and um_lis[-2] == um and um_lis[-3] == um and um_lis[-4] == um :
                        break       
                elif e == 0:
                    d, pat = valor_espe(d, pat, x1, x2)             
                    t, e, um = calculo(t, e, um, x1, x2, d, p1, p2, u, n, pat)
                    if e != 0 :
                        p1 ,p2 , u = pesos(p1, p2, u)
                        d, pat = valor_espe(d, pat, x1, x2)             
                        t, e, um = calculo(t, e, um, x1, x2, d, p1, p2, u, n, pat)
                else:
                    while e != 0 :
                        p1 ,p2 , u = pesos(p1, p2, u)
                        d, pat = valor_espe(d, pat, x1, x2)             
                        t, e, um = calculo(t, e, um, x1, x2, d, p1, p2, u, n, pat)
                        
                
    print(um)
    print(um_lis, "\n")
        

    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM compuerta_nan')    
    data = cur.fetchall()    
    
    cur2 = mysql.connection.cursor()
    cur2.execute('SELECT * FROM compuerta_nan ORDER BY it DESC LIMIT 1')
    data2 = cur2.fetchall()
    
    cur3 = mysql.connection.cursor()
    cur3.execute('SELECT Patron, x1, x2, d FROM compuerta_nan ORDER BY it DESC, Patron ASC LIMIT 4')
    data3 = cur3.fetchall()
    return render_template('nan.html', compu_nan = data, compu_nan2 = data2[0], compu_nan3 = data3)
@app.route('/nan2')
def can8():
    import random

    def calculo(t, e, um, x1, x2, x3, d, p1, p2, p3, u, n, pat):
        y = round(( ( p1 * x1) + (p2 * x2) + (p3 * x3) - u ) , 2)
        f = 0
        e = 0
        
        if y >= 0:
            f = 1
        elif y < 0:
            f = 0
        else:
            print("Hay un problema al calcular el coeficiente de aprendizaje (y)") 
              
        e = d - f
        
        v1 = n * e * x1
        v2 = n * e * x2
        v3 = n * e * x3
        
        pe1 = p1 + v1 
        pe2 = p2 + v2
        pe3 = p3 + v3

        um = round( (u - (n * e)) , 2)

        print("\n", 
            "################################","\n","Iteración ", t,"\n", "################################","\n","patron:",pat,"\n","x1:",x1,"\n", "x2:",x2,"\n", "x3:",x3,"\n","p1:",p1,"\n","p2:",p2,"\n","p3:",p3,"\n","n:",n,"\n","y:",y,"\n","f:",f,"\n","d:",d,"\n","u:",u,"\n","e:",e,"\n","v1:",v1,"\n","v2:",v2,"\n","v3:",v3,"\n","pe1:",pe1,"\n","pe2:",pe2,"\n","pe3:",pe3,"\n","um:",um,"\n",)
        
        cur = mysql.connection.cursor()
        
        cur.execute('INSERT INTO compuerta_nan2 (Patron, x1, x2,x3, p1, p2,p3,u,d, y, fx,n,e,v1,v2,v3,pe1,pe2,pe3,um,it) VALUES (%s, %s, %s,%s,%s, %s, %s,%s,%s, %s, %s, %s, %s,%s,%s, %s, %s,%s,%s,%s,%s)',
        (pat, x1, x2,x3, p1, p2,p3,u,d, y, f,n,e,v1,v2,v3,pe1,pe2,pe3,um,t))

        mysql.connection.commit()

        t += 1
        um_lis.append(um)
        return (t,  e, um)

    def valor_espe(d, pat, x1, x2, x3):
        if x1== 0 and x2==0 and x3==0:
            d = 1
            pat = 1
        elif x1== 0 and x2==0 and x3==1:
            d = 1
            pat = 2
        elif x1== 0 and x2==1 and x3==0:
            d = 1
            pat = 3
        elif x1== 0 and x2==1 and x3==1:
            d = 1
            pat = 4
        elif x1== 1 and x2==0 and x3==0:
            d = 1
            pat = 5
        elif x1== 1 and x2==0 and x3==1:
            d = 1
            pat = 6
        elif x1== 1 and x2==1 and x3==0:
            d = 1
            pat = 7
        elif x1== 1 and x2==1 and x3==1:
            d = 0
            pat = 8
        else:
            print("Error en los pesos, valores deben ser 1 o 0")
        return(d, pat)

    def pesos(p1, p2, p3, u):
        p1 = round(random.uniform(-1.0, 1.0), 2)
        p2 = round(random.uniform(-1.0, 1.0), 2)
        p3 = round(random.uniform(-1.0, 1.0), 2)
        u = round(random.uniform(-1.0, 1.0), 2)
        return (p1, p2, p3, u)


    t = 1
    d = 0
    e = 1
    p1 = 0
    p2 = 0
    p3 = 0
    u = 0
    p1 ,p2 ,p3 , u = pesos(p1, p2, p3, u)
    um_lis = [0, 0, 0, 0, 0, 0, 0, 1]
    um = 1
    pat = 0

    n = round(random.uniform(0, 1.0), 2)

    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM compuerta_nan2')
    mysql.connection.commit()

    while um_lis[-1] != um or um_lis[-2] != um or um_lis[-3] != um or um_lis[-4] != um or um_lis[-5] != um or um_lis[-6] != um or um_lis[-7] != um or um_lis[-8] != um:
        for i in [0, 1, ]:
            for j in [0, 1]:
                for k in [0, 1]:            
                    x1=i
                    x2=j 
                    x3=k 
                    
                    if um_lis[-1] == um and um_lis[-2] == um and um_lis[-3] == um and um_lis[-4] == um and um_lis[-5] == um and um_lis[-6] == um and um_lis[-7] == um and um_lis[-8] == um:
                            break       
                    elif e == 0:
                        d, pat = valor_espe(d, pat, x1, x2, x3)             
                        t, e, um = calculo(t, e, um, x1, x2, x3, d, p1, p2, p3, u, n, pat)
                        if e != 0 :
                            p1 ,p2 ,p3 , u = pesos(p1, p2, p3, u)
                            d, pat = valor_espe(d, pat, x1, x2, x3)             
                            t, e, um = calculo(t, e, um, x1, x2, x3, d, p1, p2, p3, u, n, pat)
                    else:
                        while e != 0 :
                            p1 ,p2 ,p3 , u = pesos(p1, p2, p3, u)
                            d, pat = valor_espe(d, pat, x1, x2, x3)             
                            t, e, um = calculo(t, e, um, x1, x2, x3, d, p1, p2, p3, u, n, pat)
                        
                
    print(um)
    print(um_lis, "\n")
        

    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM compuerta_nan2')    
    data = cur.fetchall()    
    
    cur2 = mysql.connection.cursor()
    cur2.execute('SELECT * FROM compuerta_nan2 ORDER BY it DESC LIMIT 1')
    data2 = cur2.fetchall()
    
    cur3 = mysql.connection.cursor()
    cur3.execute('SELECT Patron, x1, x2,x3, d FROM compuerta_nan2 ORDER BY it DESC, Patron ASC LIMIT 8')
    data3 = cur3.fetchall()
    return render_template('nan2.html', compu_nan = data, compu_nan2 = data2[0], compu_nan3 = data3)

if __name__ == '__main__':
    app.run(debug=True)