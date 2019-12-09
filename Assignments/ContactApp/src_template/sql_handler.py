from functools import wraps
import sqlite3 as sqlite
from contact import Contact

class SQLHandler:
	# TODO: add class attributes here

	def __init__(self, db_name):
		self.__conn = sqlite.connect(db_name)
		self.__create_db()

	def __del__(self):
		self.__conn.close()
	
	def cleanup_db(self):
		# TODO: code to delete all data
		pass

	def __create_db(self):
		self.__conn.execute("CREATE TABLE IF NOT EXISTS CONTACT("\
		" NAME TEXT NOT NULL PRIMARY KEY, "\
		" PHONE TEXT NOT NULL,"\
		" EMAIL TEXT)")
	
	def get_contacts(self):
		res = self.__conn.execute("select * from contact")
		return [Contact(*tup) for tup in res]
	
	def add_contact(self, contact_data):
		try:
			self.__conn.execute("INSERT INTO CONTACT VALUES(?,?,?)",(contact_data.name,
			contact_data.phone,
			contact_data.email))
			self.__conn.commit()
		except sqlite.Error:
			return False
		return True

	def delete_contact(self, contact_name):
		res = self.__conn.execute("DELETE FROM CONTACT WHERE NAME=?", (contact_name,))
		return res.rowcount != 0

	def update_contact(self, old_data, new_data):
		# TODO: Execute Update Query to udpate data. 
		pass
	
if __name__ == "__main__":
	mgr = SQLHandler('dummy.db')
	mgr.cleanup_db()
	print(mgr)
	print(mgr.get_contacts())
	
	c1 = Contact("Gaurav","9999999999","tuteur.py@gmail.com")
	c2 = Contact("Krishna","8888888888","krishna.cpp@gmail.com")
	print(mgr.add_contact(c1))
	print(mgr.add_contact(c2))
	
	for contact in mgr.get_contacts():
		print(contact)
	
	print()
	print("Delete Krishna: ", mgr.delete_contact("Krishna"))
	print("Delete Krishna Again: ", mgr.delete_contact("Krishna"))
	for contact in mgr.get_contacts():
		print(contact)