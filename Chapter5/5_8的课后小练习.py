users = ['Eric', 'Admin', 'Alex', 'John', 'Trump']
for user in users:
    if user == "Admin":
        print("Hello Admin, would you like to see a status report?\n")
    else:
        print("Hello " + user + ", thank you for logging in again\n")
