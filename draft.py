import functions
from functions import connect_db, read_query

conn, curser = connect_db("hw_solution")

"""exc.1"""
curser.execute("CREATE TABLE courses (course_id INTEGER PRIMARY KEY AUTOINCREMENT,topic TEXT,hours INTEGER);")
curser.execute("CREATE TABLE students (student_id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, email TEXT);")
curser.execute("CREATE TABLE grades (grade TEXT,student_id INTEGER,course_id INTEGER,FOREIGN KEY (student_id) REFERENCES students (student_id),FOREIGN KEY (course_id) REFERENCES courses (course_id));")

"""exc.2"""
curser.execute("INSERT INTO courses (course_id, topic, hours) VALUES(1,'Math',4),(2, 'English',2),(3,'History',1.5),(4,'Biology',3);")
curser.execute("INSERT INTO students (student_id, name,email) VALUES(1,'Emma','Emma@example.com'),(2,'John','John@example.com'),(3,'Mike','Mike@example.com'),(4,'Maya','Maya@example.com');")
curser.execute("INSERT INTO grades (grade, student_id,course_id) VALUES(80,1,1),(100,1,2),(95,1,3),(70,1,4),(88,2,1),(83,2,2),(90,2,3),(79,2,4),(98,3,1),(100,3,2),(60,3,3),(87,3,4),(68,4,1),(97,4,2),(68,4,3),(89,4,4);")

"""exc.3"""
print(read_query(curser, "SELECT course_id, avg (grade) FROM grades GROUP BY course_id;"))
