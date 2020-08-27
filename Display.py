#Display.py

#Defining a function to display the main library menu.
def menu_display():
    print('\n')
    print("""========================LIBRARY MENU=======================
                1. Display all available books.
                2. Request a book to borrow.
                3. Return a borrowed book.
                4. Exit
                """)

#Defining a function to display all the available books in the Library Catalouge.
def display_data(list_two):
    print('\n')
    print("BOOK ID \t Book Name \t\t Author Name \t\t Price")
    for every_item in list_two:
        print(every_item[0] + '\t\t' + every_item[1] + '\t\t' + every_item[2] + '\t\t' + every_item[4])
    print('\n')


#Defining a function to display the borrower's cart as per user's input.
def display_borrow(list_two):
    print('\n')
    print("BOOK ID \t Book Name \t\t Author Name \t\t Price")
    for every_item in list_two:
        print(str(every_item[0]) + '\t\t' + str(every_item[1]) + '\t\t' + str(every_item[2]) + '\t\t' + str(every_item[-1]))
    print('\n\n')

#Defining a function to display the returned items as per user's input.
def display_return(list_two):
    print('\n')
    print("BOOK ID \t Book Name \t\t Price \t\t Fine")
    for every_item in list_two:
        print(str(every_item[0]) + '\t\t' + str(every_item[1]) + '\t\t' + str(every_item[4]) + '\t\t' + '$' + str(every_item[-1]))
    print('\n\n')


# Defining function for writing the 2d list back to a inventory file. 

def write_list_to_file(list_two):
    file_one =open("Inventory.txt","w")
    for each_item in list_two:
        line = ','.join(each_item) + ('\n')
        file_one.write(line)
    file_one.close()
print('\n')    

    
