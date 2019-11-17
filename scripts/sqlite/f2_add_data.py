# Table-User: Name String (PK), Phone String
import sqlite3 as sq

conn =  sq.connect('temp.db')
def create_db():
    try:
        print(conn)
        cur = conn.cursor()
        r = cur.execute("""create table if not exists user (name string , phone string ,primary key(name))""")
        
        print(dir(r))
        cur.close()
        return True
    except sq.Error:
        return False
        
        
def insert_data():
    c = conn.cursor()
    c.execute("INSERT INTO USER VALUES(?,?)", ('pqr','1111'))
    print("Insert ", c.rowcount)
    c.close()
    conn.commit()

def get_data():
    c = conn.cursor()
    r = c.execute("SELECT * FROM USER")
    for r in c:
        print(r)
    c.close()
    
def delete_record(name):
    c=conn.cursor()
    r = c.execute("delete from user where name = ?", (name,))
    print("Deleted record" , r.rowcount)
    c.close()
    conn.commit()
    return r.rowcount != 0

print("Creating DB:", create_db())
get_data()
#insert_data()
delete_record("gaurav")
get_data()

conn.close()