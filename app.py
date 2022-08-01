import sqlite3
from flask import Flask, jsonify, request
  
app = Flask(__name__)
  
@app.route('/', methods = ['GET', 'POST'])
def home():
    if(request.method == 'GET'):
  
        data = "hello world"
        return jsonify({'data': data})
  
  
@app.route('/getdata', methods = ['POST'])
def getdata():
    name=request.form['databasename']
    tname=request.form['tablename']
    data=request.form['data']
    senddata={}
    con = sqlite3.connect(f'{name}.db')
    cur = con.cursor()
    res = cur.execute(f'SELECT * FROM {tname}')
    op=(res.fetchall())
    con.close()    
    return jsonify({'data': op})


@app.route('/creatt', methods = ['POST'])
def creatt():
    name=request.form['databasename']
    tname=request.form['tablename']
    colums=request.form['colums']
    senddata={}
    con = sqlite3.connect(f'{name}.db')
    cur = con.cursor()
    try:    
        cur.execute(f'''CREATE TABLE {tname}
                    {str(colums)}''')
    except:
        return "Error This table allready exist " 
    res = cur.execute('SELECT * FROM stocks')
    op=(res.fetchall())
    con.close()    
    return jsonify({'data': op})
  
@app.route('/execute',methods=['POST'])
def exe():
    name=request.form['databasename']
    query=request.form['query']
    con=sqlite3.connect(f'{name}.db')
    cur=con.cursor()
    try:
        cur.execute(f'{query}')
    except Exception as e:
        return jsonify({"error":f"{str(e)}"})
    return {"":"Your query executed sucessfully... "}
if __name__ == '__main__':
  
    app.run(debug = False)