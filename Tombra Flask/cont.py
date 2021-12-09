from flask import Flask, render_template,request, redirect
from db import mydb, mycursor


app = Flask(__name__)


@app.route('/')
def index():
    mycursor.execute("SELECT * FROM Person")
    people = mycursor.fetchall()
    return render_template('index.html',people = people)



@app.route('/gotoadmin')
def gotoadmin():
    mycursor.execute("SELECT * FROM Person")
    people = mycursor.fetchall()
    return render_template('adminpage.html',people = people)





@app.route('/addperson', methods=['GET', 'POST'])
def adddetail():
    if request.method == 'GET':
        return render_template('adddata.html')
    if request.method == 'POST':
          # _ = request.form['name']
        first_name = request.form['first_name']
        second_name = request.form['second_name']
        gender = request.form['gender']
        tradition = request.form['tradition']
        location = request.form['location']
        nationalid = request.form['nationalid']

        sql = 'INSERT INTO Person(first_name,second_name,gender, tradition,location,nationalid) VALUE (%s, %s,%s, %s,%s, %s)'
        val = (first_name, second_name,gender,tradition, location,nationalid)
        mycursor.execute(sql, val)
        mydb.commit()
        mycursor.execute("SELECT * FROM Person")
        people = mycursor.fetchall()
        return render_template('index.html', people = people)






@app.route('/details/<int:id>')
def customer_details(id):
    mycursor.execute(f'SELECT * FROM customers WHERE ID={id}')
    customer = mycursor.fetchone()
    return render_template('customer_detail.html', customer = customer)




@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_person(id):
    if request.method == 'GET':
        mycursor.execute(f'SELECT * FROM Person WHERE ID={id}')
        person = mycursor.fetchone()
        return render_template('editdata.html', person = person)
    if request.method == 'POST':
        first_name = request.form['first_name']
        second_name = request.form['second_name']
        gender = request.form['gender']
        tradition = request.form['tradition']
        location = request.form['location']
        nationalid = request.form['nationalid']
        sql = f'UPDATE Person SET first_name = %s, second_name = %s, gender=%s, tradition = %s, location = %s, nationalid = %s WHERE ID = %s'
        values = (first_name, second_name, gender,tradition,location,nationalid,id)
        mycursor.execute(sql, values)
        mycursor.execute("SELECT * FROM Person")
        people = mycursor.fetchall()
        mydb.commit()
        return render_template('index.html', people = people)





@app.route('/delete/<int:id>')
def delete_person(id):
    sql = f'DELETE FROM Person WHERE ID={id}'
    mycursor.execute(sql)
    mydb.commit()
    mycursor.execute("SELECT * FROM Person")
    people = mycursor.fetchall()
    return render_template('index.html', people = people)







if __name__ == '__main__':
        app.run()




