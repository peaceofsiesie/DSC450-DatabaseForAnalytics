"""
Name: Sierra Salaam
Date: June 26, 2023
Assignment: 02

"""
#Part I
# Question 4 - Vaildating String 
def validateInsert(insertvalue):
    'This function will generate the string to produce a format' #docstring
    
    insertvalue = str(insertvalue) #make sure value is a string

    reservedword = " VALUES "
    findreserveword = insertvalue.find(reservedword) #find the word VALUES
   
    if insertvalue[:12] == "INSERT INTO " and insertvalue[-1] == ";" and findreserveword != -1: #check if conditions are met
        tablename =  insertvalue[12:findreserveword-1] # assign table name
        valuename = insertvalue[findreserveword+8:-1] # assign value name
    
        print("Inserting {} into {} table".format(valuename, tablename)) #print value
        return "Inserting {} into {} table".format(valuename, tablename) #save value 
    else:
        print("Invalid Insert") #print value
        return "Invalid Insert" #save value


# Testing Out Function
def main():
    'This function will execute the results from the program' #docstring
    
    validateInsert(("INSERT INTO Students VALUES (1, 'Jane', 'B+');")) # test 1
    validateInsert("INSERT INTO Students VALUES (1, 'Jane', 'B+')") #test 2 (check for ; at the end)
    validateInsert("INSERT Students VALUES (1, 'Jane', B+);") #test 3 (check for Insert Into at beginning)
    validateInsert("INSERT INTO Phones VALUES (42, '312-667-1213');") #test 4
    validateInsert("INSERT INTO Phones VALUE (56, '616-477-1833');") # test 5 (check for values word in between)
  
    

main() #calling the main function