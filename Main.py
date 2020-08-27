#Main python File

#Other three modules are imported for execution along with datetime from Python Standard Library.
import Borrow
import Display
import Return
import datetime


#Opening the intial books file in read mode and conveting it into a 2D List for further actions.

date_time = datetime.datetime.now()

catalouge = open('Books.txt','r')
contents = catalouge.read()

list_one = contents.split('\n')
print('\n')

list_two = []

for each in list_one:
        list_two.append(each.split(','))

catalouge.close()

####################################################################################################

#Declaring a new list as return_books.
return_books = []

#Declaring a new list as borrower_cart.
borrower_cart = []


enter_name = str(input("Please enter your full name:"))
print('\n')
print("Hello" + '\t' + enter_name)
print('\n')
print('\t\t' + "Welcome to our Library.")
print('\n')




question_one = str(input("Do you wish to access our Library menu?, please enter 'Yes' or 'No':"))

#Creating the main outer loop for library menu.
                 
if question_one == "Yes":
    done = True #Using done as a flag variable
    while done == True:
        Display.menu_display()1

        #Using exceptional handling to handle any errors in the user input.
        error_handler1 = True
        while error_handler1 == True:
          try:
                choice = int(input("Enter your desired choice:"))
                

          
                if choice == 1:
                     #Calling defined function to display all the available books in the Library.
                     Display.display_data(list_two)
                
                elif choice == 2:
                         print("The books available for borrowing are as follows:")
                         Display.display_data(list_two)
                         print('\n')
                         
                         
                           
                         #Asking user input for number of books desired and their Book ID.
                         input_id = str(input("Please enter the BookID of your desired book."))

                         
                         #Calling the function that operates borrow action.
                         borrower_books = Borrow.borrow_action(list_two,input_id)

                         if len(borrower_books) > 0:
                                 #Appending the books borrowed into the borrower cart as a list.
                                 borrower_cart.append(borrower_books)

                                 #Calling previously defined function to display Borrower Cart.
                                 Display.display_borrow(borrower_cart)
                         else:
                                print('\n')
                                print('Please enter another valid Book ID.')
                                        
                                        

                           
                         
                elif choice == 3:
                         Display.display_data(list_two)
                         print('\n')

                         
                         #User input for number of books they want to return, Book id and their borrow duration.
                         input_return_id = str(input("Please enter the Book ID:"))
                         days_return = int(input("Enter the number of days since you borrowed the books:"))
                         print('\n')
                         

                         #Calling the function that operates book return action.
                         returned_items = Return.return_action(list_two,days_return,input_return_id)


                         #Appending the returned items to the previously created list(return_books), if the returned_items list is not empty.
                         if len(returned_items) > 0:
                            return_books.append(returned_items)
                            Display.display_return(return_books)
           
                                
                         else:
                            print('\n')
                            print("Invalid Book ID!Please enter a valid Book ID.")
                           

                        
                        
                           
                        
                elif choice == 4:
                     #Calling functions to write the 2D list back to inventory file.
                     Display.write_list_to_file(list_two)

                     #Calling functions to generate borrow and return notes.
                     Return.return_note(return_books,enter_name,date_time)
                     Borrow.borrow_note(borrower_cart, enter_name, date_time)

                     #Exiting the program when the user chooses to.
                     exit()

                else:
                     print('\n')
                     print("Please Enter the correct option from the menu.")
                     error_handler1 = False

          except:
                  print('\n')
                  print("Invlid Input! Please enter a valid input.")

      
                   
#Else statement when the user doesn't want to access the Library Menu and exit the program.
else:
    print('\n')
    print("Thank You. Please visit again when required.")
    exit()
            

 
                 

        

   
