from functools import wraps
import sqlite3 as sqlite
from contact import Contact

class SQLHandler:
	# TODO: add class attributes here

	def __init__(self, db_name):
		# TODO: initialize db name and create a connection to database
		pass

	def __del__(self):
		# TODO: close connection and set to None
		pass
	
	def cleanup_db(self):
		# TODO: code to delete all data
		pass

	def __create_db(self):
		# TODO: code to Create table
		pass

	def get_contacts(self):
		# TODO: Select all Data from DB. Convert Rows to Contact Objects and Return the list
		pass
	
	def add_contact(self, contact_data):
		# TODO: Insert new record in DB. Return status of insert
		pass

	def delete_contact(self, contact_name):
		# TODO: delete query for a particular contact
		pass

	def update_contact(self, old_data, new_data):
		# TODO: Execute Update Query to udpate data. 
		pass
	
if __name__ == "__main__":
	mgr = SQLHandler('dummy.db')
	mgr.cleanup_db()
	print(mgr)
	print(mgr.get_contacts())
	
	#c1 = Contact("Gaurav","9999999999","tuteur.py@gmail.com")
	#c2 = Contact("Krishna","8888888888","krishna.cpp@gmail.com")
	#print(mgr.add_contact(c1))
	#print(mgr.add_contact(c2))
	
	#for contact in mgr.get_contacts():
	#	print(contact)
	
	#print()
	#print("Delete Krishna: ", mgr.delete_contact("Krishna"))
	#print("Delete Krishna Again: ", mgr.delete_contact("Krishna"))
	#for contact in mgr.get_contacts():
	#	print(contact)