#Defining a function to operate on returnig actions and procedures.

def return_action(list_two,days_return,input_return_id):
    temp_returned_items = []
    grand_sum = 0
    for each_num in list_two:
                if each_num[0] == input_return_id:
                    #Adding the returned books into our initial inentory.
                    book_quantity = int(each_num[3]) + 1
                    each_num[3] = str(book_quantity)
                    
                    for each_value in each_num:
                        temp_returned_items.append(each_value)

                        if days_return < 10:
                              convert_ = each_num[-1].replace('$',"")
                              fl_num =  float(convert_)
                              return_fine = 0
                                            

                        elif days_return > 10:
                           convert_one = each_num[-1].replace('$',"")

                           #Calculating total fine accured on the basis of days and book price.
                           fine_duration = days_return - 10
                           fl_num1 =  float(convert_one)
                           return_fine = (0.25*(fl_num1)) * fine_duration
                           return_fine = round(return_fine,2)
                               
                    temp_returned_items.append(days_return)
                    temp_returned_items.append(return_fine)

                        
    
    return temp_returned_items


#Defining a function to generate a books returned receipt/note for the returning transaction.

def return_note(list_two,input_name,date_time):
            file_three = open("Returnnote.txt","w")
            file_three.write('==========================================================================================')
            file_three.write('\n\n')
            file_three.write('\t\t\t' + " Return Receipt:")
            file_three.write('\n\n')
            file_three.write('Current Date and Time of Transaction:' + '\t\t\t' + str(date_time))
            file_three.write('\n\n')
            file_three.write("Name:" + input_name)
            file_three.write('\n\n')
            file_three.write("BOOK ID \t Book Name \t\t Price \t\t Days Borrowed\t\t Fine")
            file_three.write('\n\n')
            grand_sum = 0
            for value in list_two:
                sign_remove = value[4].replace('$',"")
                value[4] = float(sign_remove)
                grand_sum = value[4] + value[-1] + grand_sum
                grand_sum = round(grand_sum,2)
                file_three.write(str(value[0]) + '\t\t' + str(value[1]) + '\t\t' + '$' + str(value[4]) + '\t\t\t' + str(value[5])+ '\t\t\t' + '$' + str(value[-1])+'\n')  
            file_three.write('\n\n')
            file_three.write('-----------------------------------------------------------------------------------------------')
            file_three.write('\n')
            file_three.write("Grand Total:" + '\t\t\t\t\t\t' + '$' + str(grand_sum))
            file_three.write('\n\n')
            file_three.write('================================================================================================')
            file_three.close()
                
