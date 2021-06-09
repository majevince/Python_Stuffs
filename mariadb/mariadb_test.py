import mariadb
import sys
import mariadb


try:
    
    conn = mariadb.connect(
        user="admin",
        password="majevince",
        host="127.0.0.1",
        port=3306,
        database="vince_data"
        )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

# Get Cursor
cur = conn.cursor()



# Create SQL Table
cur.execute("""
CREATE TABLE IF NOT EXISTS Operators (
    SN INTEGER AUTO_INCREMENT PRIMARY KEY,
    Operator TEXT,
    vendor TEXT,
    host_country TEXT,
    year INTEGER
)
""")
# Inster Data into SQL Tables
cur.execute("""
INSERT INTO Operators VALUES 
(1, 'vodacom', 'Nokia', 'Finland', 19),
(2, 'Telefonokia', 'huawei', 'Italy', 28),
(3, 'Vvrizon', 'Ericson', 'US', 30)
""")

# Select Data from SQL Tables

cur.execute("""
SELECT * FROM Operators, students
""")


# Create SQL Table
cur.execute("""
CREATE TABLE IF NOT EXISTS students (
    first_name TEXT,
    middle_name TEXT,
    last_name TEXT,
    age INTEGER
)
""")
# Inster Data into SQL Tables
cur.execute("""
INSERT INTO students VALUES 
('Alhamdu', 'Umaru', 'Bello', 22),
('Vincent', 'Anyah', 'Ojomaje', 18),
('Haruna', 'Umar', 'Adoga', 20)
""")

rows = cur.fetchall()
print(rows)

conn.commit()
conn.close()
