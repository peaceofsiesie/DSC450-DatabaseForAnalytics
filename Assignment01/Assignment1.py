"""
Name: Sierra Salaam
Date: June 18, 2023
Assignment: 01

"""
#Part I
# Question A - read file, collect all numbers in file, calculate the average
def calculateavg(fileinput):
    'The function will generate the calculation of the average' #docstring
    numlst = []

    f = open(fileinput, "r")
    lines = f.readlines()
    f.close()
    
    for x in lines:
        for num in x.split(","):
            numlst.append(int(num))

    averagenum = sum(numlst) / len(numlst)
    return averagenum

# Question B - read file, create new file and write in new file 
def randwnewfile(fileinput):
    'This function will create a new file and write into file' #doctring
    f = open(fileinput, "r")
    tempnum = f.read()
    f.close()

    newf = open("newnumfile.txt", "w")
    for x in tempnum.split(","):
        newf.write(x.strip() + "\n")

# Question C - Generate and return a SQL Insert Statment 
def generateInsert(tablename, valuelst):
    'This function will generate the string to produce a format' #docstring
    
    for i in range(len(valuelst)):
        if str(valuelst[i]).isnumeric():
            valuelst[i] = int(valuelst[i])
            
    return "INSERT INTO {} VALUES {};".format(tablename, valuelst)

# Testing Out Function
def main():
    'This function will execute the results from the program'
    #calculateavg("numberfile.txt") # testing out Question A
    #randwnewfile("numberfile.txt") # testing out Question B
    print(generateInsert('Students',[1, 'Jane', 'B+'])) #testing out Question C - Test 1
    print(generateInsert('Phones', ['42', '312-557-1212'])) #testing out Question C - Test 2
  
    

main() #calling the main function