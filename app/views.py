from flask import render_template, flash, request,url_for,redirect,flash
from app import app
import sqlite3
@app.route('/')
def table():
     
    return render_template('table.html')
@app.route('/view',methods=['GET' ,'POST'])
def view():
	if request.method =='GET':
	
		db=sqlite3.connect('students.db')
		cursor = db.execute("SELECT * FROM students ORDER BY id")
		rows=[]
		for row in cursor:
	   		rows.append(row)
		return render_template('view.html',
                               rows=rows)
	else:
        	if request.form['delete'] != '':
			db=sqlite3.connect('students.db')
		
			db.execute("DELETE FROM students WHERE name =(?)",  ((request.form['delete'],)))
			db.commit()
			db.close()
			return redirect('/view')
		
		elif request.form['search'] !='':
			db=sqlite3.connect('students.db')
		
			cursor1=db.execute("SELECT * FROM students WHERE name=(?)",((request.form['search'],)))
			rows=[]
			for row in cursor1:
				rows.append(row)
			db.close()
			return render_template('search.html',rows=rows)
		return redirect('/view')
	
	
@app.route('/add' , methods=['GET', 'POST'])
def add():
	if request.method == 'POST':
        	db=sqlite3.connect('students.db')
		db.execute('''INSERT INTO students VALUES(?,?,?,?) ''',
		(request.form['id'], request.form['name'] ,request.form['age'], request.form['mark']));
		db.commit()
		db.close()
		return redirect('/view')
	return render_template('add.html')


	 
