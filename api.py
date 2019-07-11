from __future__ import print_function
import mysql.connector
from flask import Flask, render_template, request, redirect, url_for,send_from_directory, jsonify
from flask import session
import time

app = Flask(__name__)
app.secret_key = "sysall14"

@app.route("/")
def main():
    mydb = mysql.connector.connect(
        host="127.0.0.1",
        user="ade",
        passwd="Jenkins0",
        database="auction"
    )
    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM `clients` ORDER BY date DESC")
    data = mycursor.fetchall()
    bidding = []
    for el in data:
        nom = el[1]
        prix = el[4]
        date = el[5]
        bidding.append({
            "nom": nom,
            "prix": prix,
            "date":date
        })

    mycursor.execute("SELECT MAX(prix) FROM clients")
    data =mycursor.fetchall()
    for el in data:
        maxBid = el[0]

    return render_template('index.html', data=bidding, max = maxBid)



@app.route('/upload', methods=['POST','GET'])
def upload():
    mydb = mysql.connector.connect(
        host="127.0.0.1",
        user="ade",
        passwd="Jenkins0",
        database="auction"
    )
    mycursor = mydb.cursor()

    mycursor.execute("SELECT MAX(prix) FROM clients")
    data = mycursor.fetchall()
    for el in data:
        maxBid = el[0]

    if request.method == 'POST':
        _result = request.form.to_dict()

    nom = _result['nom']
    email= _result['email']
    prix = int(_result['price']) + maxBid
    tel = _result['numero']
    date = time.strftime('%Y-%m-%d %H:%M:%S')

    session['nom'] = nom
    session['email'] = email
    session['telephone'] = tel

    if 'nom' in session:
        name = session['nom']
    if 'email' in session:
        mail = session['email']
    if 'telephone' in session:
        telephone = session['telephone']

    sql = "INSERT INTO clients (nom,email,telephone,prix,date) VALUES (%s, %s, %s, %s, %s)"
    val = (nom,email,tel,prix,date)
    mycursor.execute(sql, val)

    mydb.commit()

    print(mycursor.rowcount, "record inserted.")

    mycursor.execute("SELECT * FROM `clients` ORDER BY date DESC")
    data = mycursor.fetchall()
    bidding = []
    for el in data:
        nom = el[1]
        prix = el[4]
        date = el[5]
        bidding.append({
            "nom": nom,
            "prix": prix,
            "date": date
        })

    mycursor.execute("SELECT MAX(prix) FROM clients")
    data = mycursor.fetchall()
    for el in data:
        maxBid = el[0]

    return render_template('index.html', data=bidding, data1 = name, data2 = mail, data3 = telephone,max = maxBid)

@app.route('/upload1', methods=['POST','GET'])
def upload1():
    mydb = mysql.connector.connect(
        host="127.0.0.1",
        user="ade",
        passwd="Jenkins0",
        database="auction"
    )
    mycursor = mydb.cursor()

    if request.method == 'POST':
        _result = request.form.to_dict()

    nom = _result['nom']
    prenom = _result['prenom']
    email= _result['email']
    tel = _result['numero']


    sql = "INSERT INTO alerte (nom,prenom,email,telephone) VALUES (%s, %s, %s, %s)"
    val = (nom,prenom,email,tel)
    mycursor.execute(sql, val)

    mydb.commit()

    print(mycursor.rowcount, "record inserted.")

    mycursor.execute("SELECT * FROM `clients` ORDER BY date DESC")
    data = mycursor.fetchall()
    bidding = []
    for el in data:
        nom = el[1]
        prix = el[4]
        date = el[5]
        bidding.append({
            "nom": nom,
            "prix": prix,
            "date": date
        })

    mycursor.execute("SELECT MAX(prix) FROM clients")
    data = mycursor.fetchall()
    for el in data:
        maxBid = el[0]

    return render_template('index.html', data=bidding,max = maxBid)


@app.route('/upload2', methods=['POST','GET'])
def upload2():
    mydb = mysql.connector.connect(
        host="127.0.0.1",
        user="ade",
        passwd="Jenkins0",
        database="auction"
    )
    mycursor = mydb.cursor()

    if request.method == 'POST':
        _result = request.form.to_dict()

    email= _result['email']
    message = _result['message']


    sql = "INSERT INTO newletter (message,email) VALUES (%s, %s)"
    val = (message,email)
    mycursor.execute(sql, val)

    mydb.commit()

    print(mycursor.rowcount, "record inserted.")

    mycursor.execute("SELECT * FROM `clients` ORDER BY date DESC")
    data = mycursor.fetchall()
    bidding = []
    for el in data:
        nom = el[1]
        prix = el[4]
        date = el[5]
        bidding.append({
            "nom": nom,
            "prix": prix,
            "date": date
        })
    mycursor.execute("SELECT MAX(prix) FROM clients")
    data = mycursor.fetchall()
    for el in data:
        maxBid = el[0]

    return render_template('index.html', data=bidding, max = maxBid)


if __name__ == "__main__":
    app.run(debug=True)



