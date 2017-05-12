import calender_events.py
import get.py

while True:
	print ("Welcome to Caleder:")
	print ("Calender Actions:")
	print ("1. Create Calender")
	print ("2. Add Task to calender")
	print ("3. View all tasks in caleneder")
	print ("4. View last Task")
	print ("5. QUIT!")
	print ("Please enter a number corresponing to the action: ")
	user_input = input("Please Enter a Number that corresponds to the action: " )

	if user_input == '5':
		break 
	elif user_input == '1':
		print ("it works")
	elif user_input == '2':
		username = input("Please enter username: ")
		date = input("Please enter date:" )
		event = input("Please enter event: ")
		creat_event(username,date,event)
	elif user_input == '3':
		username = input("Please enter username: ")
		get_data(username)
		
	elif user_input == '4':
		
		


 