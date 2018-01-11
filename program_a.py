file_name = input("Enter file name ")
table = open(file_name,"r",1)
print("Name of the file: ", table.name)
File_content = table.readlines()
length = len(File_content)
fields = File_content[0].split(',')
num = len(fields)
print("The different fields in this data file are: ")
j=0;
while j<num:
    print(fields[j])
    j=j+1
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
table.close()
