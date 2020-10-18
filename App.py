from flask import Flask, render_template
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'osman'
app.config['MYSQL_PASSWORD'] = 'armando9812'
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

        um = u - (n * e)

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
        p1 = random.uniform(-1.0, 1.0)
        p2 = random.uniform(-1.0, 1.0)
        u = random.uniform(-1.0, 1.0)
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
    n = random.uniform(0, 1.0)
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
                else:
                    p1 ,p2 , u = pesos(p1, p2, u)
                    d, pat = valor_espe(d, pat, x1, x2)             
                    t, e, um = calculo(t, e, um, x1, x2, d, p1, p2, u, n, pat)
                        
                
    print(um)
    print(um_lis, "\n")
           
    
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM compuerta_an')    
    data = cur.fetchall()    
    return render_template('and.html', compu_and = data)

if __name__ == '__main__':
    app.run(debug=True)