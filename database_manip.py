import sqlite3

# Creates or opens a file called student_db with a SQLite3 DB
db = sqlite3.connect('data/student.db')
cursor = db.cursor()

# Get a cursor object
cursor.execute('''CREATE TABLE python_programming(id INTEGER PRIMARY KEY, name TEXT, grade INTEGER)''')
db.commit()

name1 = 'Carl Davis'
grade1 = 61
id1 = 55

name2 = 'Dennis Fredrickson'
grade2 = 88
id2 = 66

name3 = 'Jane Richards'
grade3 = 78
id3 = 77

name4 = 'Peyton Sawyer'
grade4 = 45
id4 = 12

name5 = 'Lucas Brooke'
grade5 = 99
id5 = 2

student_grades = [(id1, name1, grade1), (id2, name2, grade2), (id3, name3, grade3), (id4, name4, grade4), (id5, name5, grade5)]

cursor.executemany('INSERT INTO python_programming(id, name, grade) VALUES(?,?,?)', student_grades)
db.commit()

# Execute the SELECT statement
cursor.execute('SELECT * FROM python_programming WHERE grade BETWEEN 60 AND 80')

# Fetch all the records
records = cursor.fetchall()

# Print the records
for record in records:
    print(record)

# Update Carl Davis's grade
new_grade = 65
cursor.execute("UPDATE python_programming SET grade = ? WHERE name = ?", (new_grade, "Carl Davis"))
db.commit()

# Delete Dennis Fredrickson's row
cursor.execute("DELETE FROM python_programming WHERE name = 'Dennis Fredrickson'")
db.commit()

# Change the grade of people with an ID below 55
new_grade = 90
cursor.execute('UPDATE python_programming SET grade=? WHERE id < ?', (new_grade, 55))
db.commit()

# Close the cursor and the database connection
cursor.close()
db.close() 
