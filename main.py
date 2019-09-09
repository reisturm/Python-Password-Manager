from functions import storeInfo, checkDatabase, initializeDb, changeInfo, removeFromDb, makePassword, generatePassword

redo = 'y'
changes = False

db = {}
initializeDb(db)
s = []
for service in db:
    s.append(service)

print("Welcome to your password manager.")
while redo == 'Y' or redo == 'y':
    print("\nWhat would you like to do?")
    print("1: List stored services. \n"
          "2: Store an email and password. \n"
          "3: Verify a password for website. \n"
          "4: Update information for a website/service. \n"
          "5: Delete an entry. \n"
          "6: Generate a password. \n"
          "0: Exit Program.")
    choice = input("")
    if choice == '1':
        if not s:
            print("No services currently stored.")
        else:
            print(", ".join(s))

    elif choice == '2':
        redo2 = 'y'
        while redo2 == 'y' or redo2 == 'Y':
            service = input("What service do you want to store your email/password for? ")
            emailUser = input("What is the email/username associated with the account? ").encode('utf-8')
            pw = input("What is the password for this account? ").encode('utf-8')
            storeInfo(service, emailUser, pw, db,s)
            changes = True
            redo2 = input("\nWould you like to store something else? (y/n) ")
        redo = input("\nDo you need anything else? (y/n) ")

    elif choice == '3':
        redo3 = 'y'
        while redo3 == 'y' or redo3 == 'Y':
            service = input("What service are you verifying your password for? ")
            emailUser = input("What email is associated with the account of interest? ")
            pw = input("Enter your password. ")
            checkDatabase(service, emailUser.encode('utf-8'), pw.encode('utf-8'), db)
            changes = True
            redo3 = input("\nDo you need verify anything else? (y/n) ")
        redo = input("\nDo you need anything else? (y/n) ")

    elif choice == '4':
        redo4 = 'Y'
        while redo4 == "y" or redo4 == "Y":
            service = input("What service are you updating your information for? ")
            emailUser = input("What is the new email/username for your account? ").encode('utf-8')
            pw = input("What is the new password for your account? ").encode('utf-8')
            changeInfo(service, emailUser, pw, db)
            changes = True
            redo4 = input("\nWould you like to update something else? (y/n) ")
        redo = input("\nDo you need anything else? (y/n) ")

    elif choice == '5':
        redo5 = 'y'
        while redo5 == 'y' or redo5 == 'Y':
            print("\nServices you have currently stored are: " + ", ".join(s))
            service = input("Which service do you wish to remove from the list? ")
            removeFromDb(service, db,s)
            changes = True
            redo5 = input("Would you like to delete more entries? ")

        redo = input("\nDo you need anything else? (y/n) ")

    elif choice == '6':
        redo6 = 'y'
        while redo6 == 'y' or redo6 == 'Y':
            service = input("What service are you making an account for? ")
            pw = input("Enter a word to generate a random password. ")
            while True:
                length = int(input("How long do you want your password to be? (10-15) "))
                if length < 10:
                    print("Password too short.")
                elif length > 15:
                    print("Password too long.")
                else:
                    break
            pw = generatePassword(service.encode('utf-8'), pw.encode('utf-8'), length)
            print("The randomly generated password is " + pw + ".")
            print("-----------------------------------------")
            print("PLEASE KEEP IT IN A SAFE PLACE")
            print("-----------------------------------------")
            store = input("Would you like to store this password? (y/n) ")
            if store == "y" or store == "Y":
                emailUser = input("What is the email/username for the service? ")
                storeInfo(service, emailUser.encode('utf-8'), pw.encode('utf-8'), db, s)
                changes = True
            redo6 = input("Would you like to make another password? (y/n) ")
        redo = input("\nDo you need anything else? (y/n) ")
    elif choice == '0':
        break
    else:
        print("Invalid input. Please try again.")

if changes:
    open('db.txt', 'w').close()
    file = open("db.txt", "a", encoding='utf-8')
    for service in db:
        file.write(service + "," + db[service][0] + "," + db[service][1] + '\n')

    file.close()
