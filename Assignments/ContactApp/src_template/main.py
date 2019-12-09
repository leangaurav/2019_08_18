from contact import Contact
from contact_manager import ContactManager

main_menu = "1. View\n2. Insert\n3. Delete\n4. Update\n5. Exit\n Enter(1-5):"

mgr = ContactManager()

def view():
	print("\n View Menu\n 1. Find by name\n 2. Search\n 3. View All")
	ch = input("Enter(1-3):")
	
	if ch == '1':
		pass
	elif ch == '2':
		pass
	elif ch == '3':
		c = mgr.get_contacts()
		if c:
			for contact in c:
				print(contact)
		else:
			print("Contact list is empty !!")
	else:
		print("Wrong Input !!\n")
	
def insert():
	n = input("Enter Name:")
	p = input("Enter Phone:")
	e = input("Enter Email:")
	
	c = Contact(n,p,e)
	
	if mgr.add_contact(c):
		print("\n Added new contact !")
	else:
		print("\n Cannot add this contact !")
	
	
	
def delete():
	name = input("Enter name to delete:")
	
	res = mgr.delete_contact(name)
	if res:
		print("Contact Deleted!")
	else:
		print("Cannot delete!")
	
def update():
	pass

def main():
	d = {"1":view, "2":insert, "3": delete ,"4":update , "5":exit}
	while True:
		print(main_menu)
		ch = input()
		
		if ch in d:
			d[ch]()
		else:
			print("\nInvalid input!!")

if __name__ == '__main__':
	main()
