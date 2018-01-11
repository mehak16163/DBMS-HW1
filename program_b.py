import sys

# Reading metadata to create datafile
meta_file_name = input("Enter name of the file: ")
meta_table = open(meta_file_name, "r", 1)

print("Name of the file: ", meta_table.name)
metadata = meta_table.readlines()
size = len(metadata)

fielddata = []

for i in range (0, size):
    fielddata.append(metadata[i])

user_data = open("Datafile.txt", "r", 1)
userdata = user_data.readlines()
fields = userdata[0].split(',')
total_size = len(userdata)

firstline = ""
for i in range (0, size):
    String = fielddata[i].split(',')[0]
    if(i == size - 1):
        firstline = firstline + String
    else:
        firstline = firstline + String + ','

firstline = firstline + '\n'

with open("NewUserFile.txt", "w") as file:
    file.write(firstline)
    for i in range (1, total_size):
        string = userdata[i]
        info = string.split(',')
        newstring = ""
        for j in range (0, size):
            respdata = fielddata[j].split(',')
            for k in range (0, size):
                if respdata[0] == fields[k]:
                    break
            teststring = info[k][0:int(respdata[2].rstrip())]
            if(j == size - 1):
                newstring = newstring + teststring
            else:
                newstring = newstring + teststring + ','
        newstring = newstring + '\n'
        file.write(newstring)

# same code as program 1
table = open("NewUserFile.txt","r",1)
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


