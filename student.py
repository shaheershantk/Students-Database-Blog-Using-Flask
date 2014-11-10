import sqlite3

conn = sqlite3.connect('students.db')
c = conn.cursor()

# Create table
c.execute('''CREATE TABLE students
             (id int, name text, age int, marks int)''')

# Insert a row of data
c.execute("INSERT INTO students VALUES (1,'Shaheer',23,80)")

# Save (commit) the changes
conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()
