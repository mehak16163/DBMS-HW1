import sys
import time

start = time.time()
file_name = input("Enter file name ")
table = open(file_name,"r",1)
print("Name of the file: ", table.name)
File_content = table.readlines()
end = time.time()
time_elapsed = end - start
print("Time elapsed for reading: " + str(time_elapsed))

length = len(File_content)
fields = File_content[0].split(',')
num = len(fields)
print("The different fields in this data file are: ")
j=0;
while j<num:
    print(fields[j])
    j=j+1
j=0;
print("Select one of the two options:\n1. Print entire content\n2. Find sum of a field")
option = int(input("The option is: "))
if option == 1:
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
else:
    print("Select the field")
    f = input("")
    f=f.lower()
    j=0
    while j<num:
        if f == fields[j].lower().lstrip().rstrip():
            break
        j=j+1
    if j==num:
        print("No such field exists")
        sys.exit("")
    check = File_content[1].split(',')[j]
    try:
        val = float(check)
    except ValueError:
        print("This field is not numeric")
        sys.exit("")
    i=1
    result=0
    while i<length:
        result = result + float(File_content[i].split(',')[j])
        i=i+1;
    print("The sum is " , result)
table.close()