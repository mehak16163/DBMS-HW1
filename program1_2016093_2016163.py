import sys
import time

start = time.time()//for calculating time
file_name = input("Enter file name ")
table = open(file_name,"r",1)
print("Name of the file: ", table.name)
File_content = table.readlines()//reading the contents of the file
end = time.time()
time_elapsed = end - start//time taken to read the data
print("Time elapsed for reading: " + str(time_elapsed))

length = len(File_content)//No. of rows in the data file
fields = File_content[0].split(',')
num = len(fields)//No. of fields in each row
print("The different fields in this data file are: ")
j=0;
while j<num://printing the different field names in the data file
    print(fields[j])
    j=j+1
j=0;
print("Select one of the two options:\n1. Print entire content\n2. Find sum of a field")//asking user for the option 
option = int(input("The option is: "))
if option == 1://printing the content of the file on the console
    i=0;         
    while i<length:
        field = File_content[i].split(',')
        nums = len(field)
        k=0;
        while k<nums:
            print(field[k],end=' ')
            k=k+1
        print("")
        i=i+1
else://finding sum of the field
    print("Select the field")
    f = input("")
    f=f.lower()
    j=0
    while j<num:
        if f == fields[j].lower().lstrip().rstrip():
            break
        j=j+1
    if j==num:
        print("No such field exists")//if the field name is wrong
        sys.exit("")
    check = File_content[1].split(',')[j]
    try:
        val = float(check)//checking wether the field is numeric or not
    except ValueError:
        print("This field is not numeric")
        sys.exit("")
    i=1
    result=0
    while i<length://finding the sum of the field
        result = result + float(File_content[i].split(',')[j])
        i=i+1;
    print("The sum is " , result)//printing the result
table.close()//closing the opened file
