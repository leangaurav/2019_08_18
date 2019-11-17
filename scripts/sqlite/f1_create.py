# Table-User: Name String (PK), Phone String
import sqlite3 as sq

def create_db():
    try:
        with sq.connect('temp.db') as conn:
            print(conn)
            cur = conn.cursor()
            r = cur.execute("""create table if not exists user (name string , phone string ,primary key(name))""")
            
            print(dir(r))
            cur.close()
            return True
    except sq.Error:
        return False
        
print("Creating DB:", create_db())