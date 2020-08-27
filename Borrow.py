
#Defining a function to carry out all the borrow actions and procedures. 

def borrow_action(list_two,input_id):
         temp_borrower_cart = []
         
         for each_value in list_two:
              if each_value[0] == input_id:
                              if int(each_value[3]) > 0:
                                   #Decreasing the quantity of the requested book in the inventory.
                                    quantity_book = int(each_value[3]) - 1
                                    each_value[3] = str(quantity_book)
                                    for each_num in each_value:
                                      #Appending the requested book details to the borrower's cart.
                                      temp_borrower_cart.append(each_num)
                                     

                                    
                              elif int(each_value[3]) < 0 or int(each_value[3]) == 0:
                                        print('\n')
                                        print("Sorry for the inconvenience. We do not have the requested book at the moment.")     
         
         return temp_borrower_cart
        
#Defining a function to generate a borrower receipt note for borrow transaction.         

def borrow_note(list_two, enter_name, date_time):
            file_two = open("Borrownote.txt", "w")
            file_two.write('=============================================================')
            file_two.write('\n\n')
            file_two.write('\t\t\t' + " Borrower Receipt:")
            file_two.write('\n\n')
            file_two.write("Current Date and Time of transcation:" + '\t\t' +  str(date_time))
            file_two.write('\n\n')
            file_two.write("Name:" + enter_name)
            file_two.write('\n\n')
            file_two.write("Book ID \t Book Name \t\t Price")
            file_two.write('\n\n')
            sum_ = 0
            for value in list_two:
                sign_remove = value[-1].replace('$',"")
                value[-1] = float(sign_remove)
                sum_ = value[-1] + sum_
                sum_ = round(sum_,2)
                file_two.write(str(value[0]) + '\t\t' + str(value[1]) + '\t\t' +'$' + str(value[-1]) + '\t' + '\n')
            file_two.write('\n\n')
            file_two.write('------------------------------------------------------------')
            file_two.write('\n')
            file_two.write("Grand Total:" + '\t\t\t\t\t' + '$' + str(sum_))
            file_two.write('\n\n')
            file_two.write("Note: All books must be returned within 10 days.")
            file_two.write('\n\n')
            file_two.write('===========================================================')
            file_two.close()
